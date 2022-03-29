import dataclasses as dataclasses
from datetime import date
from typing import Optional, List

from allocation.domain import event, command


class OutOfStock(Exception):
    pass


@dataclasses.dataclass(unsafe_hash=True)
class OrderLine:
    orderId: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date] = None):
        self.ref = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.ref == self.ref

    def __hash__(self):
        return hash(self.ref)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line):
        if self.sku == line.sku and self.available_qty >= line.qty:
            return True

    @property
    def allocated_qty(self):
        return sum(t.qty for t in self._allocations)

    @property
    def available_qty(self) -> int:
        return self._purchased_quantity - self.allocated_qty

    def to_json(self):
        json_comment = {
            "ref": self.ref,
            "sku": self.sku,
            "available_qty": self.available_qty
        }
        return json_comment

    def deallocate_one(self):
        return self._allocations.pop()


class Product:
    def __init__(self, sku: str, batches: List[Batch], version: int = 0):
        self.sku = sku
        self.batches = batches
        self.version = version
        self.events = []

    def allocate(self, line):
        try:
            batch = next(b for b in self.batches if b.can_allocate(line))
            batch.allocate(line)
            self.version += 1
            self.events.append(event.Allocated(
                line.orderId,
                line.sku,
                line.qty,
                batch.ref
            ))
            return batch.ref
        except StopIteration:
            self.events.append(event.OutOfStock(line.sku))

    def change_batch_quantity(self, ref: str, qty: int):
        try:
            batch = next(b for b in self.batches if b.ref == ref)
            batch._purchased_quantity = qty
            while batch.available_qty < 0:
                line = batch.deallocate_one()
                self.events.append(command.Allocate(line.orderId, line.sku, line.qty))
        except StopIteration:
            self.events.append(
                event.InvalidBatchRef(ref)
            )

    def to_json(self):
        json_comment = {
            "sku": self.sku,
            "batches": [b.to_json() for b in self.batches],
            "version": self.version
        }
        return json_comment

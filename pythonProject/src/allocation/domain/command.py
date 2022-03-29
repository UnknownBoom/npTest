import dataclasses
from datetime import date


class Command:
    pass


@dataclasses.dataclass
class Allocate(Command):
    orderid: str
    sku: str
    qty: int


@dataclasses.dataclass
class ChangeBatchSize(Command):
    ref: str
    qty: int


@dataclasses.dataclass
class CreateBatch(Command):
    ref: str
    sku: str
    qty: int
    eta: date = None


@dataclasses.dataclass
class List(Command):
    pass


@dataclasses.dataclass
class Delete(Command):
    ref: str

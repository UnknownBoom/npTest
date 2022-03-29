import dataclasses

from allocation.adapters.email import send_email
from allocation.domain import command, event
from allocation.service.unit_of_work import BaseUnitOfWork
from src.allocation.domain.model import Batch, Product, OrderLine


@dataclasses.dataclass
class InvalidSku(Exception):
    message: str


def is_valid_sku(sku, batches):
    return sku in (b.sku for b in batches)


def allocate(cmd: command.Allocate, uow: BaseUnitOfWork):
    with uow:
        product = uow.repo.get(cmd.sku)
        if not product:
            raise InvalidSku(f'Invalid sku: {cmd.sku}')
        batchref = product.allocate(OrderLine(cmd.orderid, cmd.sku, cmd.qty))
        uow.commit()
        return batchref


def delete_(cmd: command.Delete, uow: BaseUnitOfWork):
    with uow:
        repo = uow.repo
        repo.delete(cmd.ref)
        uow.commit()


def list_(cmd: command.List, uow: BaseUnitOfWork):
    with uow:
        return uow.repo.list()


def create_(cmd: command.CreateBatch, uow: BaseUnitOfWork):
    with uow:
        repo = uow.repo
        product = repo.get(cmd.sku)
        if not product:
            product = Product(cmd.sku, [])
            uow.repo.add(product)
        batch = Batch(cmd.ref, cmd.sku, cmd.qty, cmd.eta)
        product.batches.append(batch)
        uow.commit()
    return batch


def email_handler(email, uow):
    send_email(email)


def change_batch_size(cmd: command.ChangeBatchSize, uow: BaseUnitOfWork):
    with uow:
        product = uow.repo.get_by_batch_ref(cmd.ref)
        product.change_batch_quantity(cmd.ref, cmd.qty)
        uow.commit()


CMD_HANDLERS = {
    command.List: list_,
    command.CreateBatch: create_,
    command.Allocate: allocate,
    command.Delete: delete_,
    command.ChangeBatchSize: change_batch_size,
}  # type: Dict[Type[Command], Callable]

EVENT_HANDLERS = {
    event.MailEvent: [email_handler],
    event.Allocated: [email_handler],
    event.InvalidBatchRef: [email_handler],
    event.OutOfStock: [email_handler],
}  # type: Dict[Type[Event], List[Callable]]

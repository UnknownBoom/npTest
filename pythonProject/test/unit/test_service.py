from allocation.adapters import repo
from allocation.domain.model import OrderLine
from allocation.service import unit_of_work


class FakeRepository(batch_repo.BaseRepo):
    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, ref):
        return next(b for b in self._batches if b.ref == ref)

    def list(self):
        return list(self._batches)


    def delete(self, ref: str):
        self._batches.remove(next(b for b in self._batches if b.ref == ref))


class FakeUnitOfWork(unit_of_work.BaseUnitOfWork):
    def __init__(self):
        self.repo = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_batches():
    uow = FakeUnitOfWork()
    services.create_batch(ref='b-1', sku='TEST!', qty=100, uow=uow)
    assert uow.committed
    assert uow.repo.get('b-1') is not None


def test_allocation():
    uow = FakeUnitOfWork()
    batch = services.create_batch(ref='b-1', sku='TEST!', qty=100, uow=uow)
    services.allocate(OrderLine('1', 'TEST!', 100), uow)

    assert batch.allocated_qty == 100


# def test_list_batches():
#     uow = FakeUnitOfWork()
#     services.create_batch(ref='b-1', sku='TEST!', qty=100, uow=uow)
#     assert uow.committed
#     assert uow.repo.get('b-1') is not None
#
#
# def test_delete_batches():
#     uow = FakeUnitOfWork()
#     services.create_batch(ref='b-1', sku='TEST!', qty=100, uow=uow)
#     assert uow.committed
#     assert uow.repo.get('b-1') is not None
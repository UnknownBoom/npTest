import typing

import sqlalchemy.orm

from src.allocation.domain import model


class BaseRepo:
    def add(self, product: model.Product):
        raise NotImplementedError

    def get(self, sku: str) -> model.Product:
        raise NotImplementedError

    def delete(self, ref: str):
        raise NotImplementedError

    def list(self) -> typing.List[model.Product]:
        raise NotImplementedError

    def get_by_batch_ref(self, ref):
        raise NotImplementedError


class EventTrackingRepo:
    def __init__(self, repo: BaseRepo):
        self.repo = repo
        self.seen = []

    def add(self, batch: model.Product):
        product = self.repo.add(batch)
        if product:
            self.seen.append(product)

    def get(self, ref: str) -> model.Product:
        product = self.repo.get(ref)
        if product:
            self.seen.append(product)
        return product

    def delete(self, ref: str):
        self.repo.delete(ref)

    def list(self) -> typing.List[model.Product]:
        products = self.repo.list()
        if products:
            for product in products:
                self.seen.append(product)
        return products

    def get_by_batch_ref(self, ref):
        product = self.repo.get_by_batch_ref(ref)
        if product:
            self.seen.append(product)
        return product


class AlchemyRepo(BaseRepo):

    def __init__(self, session: sqlalchemy.orm.Session):
        self.session = session

    def add(self, product: model.Product):
        return self.session.add(product)

    def get(self, sku: str) -> model.Product:
        return self.session.query(model.Product).filter_by(sku=sku).first()

    def delete(self, sku: str):
        return self.session.query(model.Product).filter_by(sku=sku).delete()

    def list(self) -> typing.List[model.Product]:
        return self.session.query(model.Product).all()

    def get_by_batch_ref(self, ref) -> model.Product:
        return (self.session
                .query(model.Product)
                .join(model.Batch)
                .where(ref == ref)
                .first()
                )

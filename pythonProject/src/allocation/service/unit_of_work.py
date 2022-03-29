from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from allocation.adapters.repo import BaseRepo, EventTrackingRepo
from src.allocation.adapters import repo
from src.allocation.config import config


class BaseUnitOfWork:
    repo: BaseRepo = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rollback()

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError


class EventTrackingUnitOfWork(BaseUnitOfWork, ABC):
    repo: EventTrackingRepo = None

    def collect_new_events(self):
        for p in self.repo.seen:
            while p.events:
                yield p.events.pop(0)


DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(config.get_postgres_config()))


class ProductUoW(EventTrackingUnitOfWork):

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.repo = repo.EventTrackingRepo(repo.AlchemyRepo(self.session))
        return super().__enter__()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

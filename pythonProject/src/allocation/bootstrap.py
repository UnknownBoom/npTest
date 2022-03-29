import inspect

from sqlalchemy import create_engine

from allocation.adapters import orm
from allocation.config import config
from allocation.service import handlers, messagebus, unit_of_work
from service.unit_of_work import BaseUnitOfWork


def bootstrap(uow: BaseUnitOfWork = unit_of_work.ProductUoW()):
    orm.start_mappers()
    engine = create_engine(config.get_postgres_config())
    orm.metadata.create_all(engine)

    dependencies = {'uow': uow}

    injected_event_handler = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }

    injected_command_handler = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.CMD_HANDLERS.items()
    }

    return messagebus.MessageBus(uow, injected_event_handler, injected_command_handler)


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)

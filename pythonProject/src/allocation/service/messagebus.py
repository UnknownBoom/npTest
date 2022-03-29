from typing import Union, Dict, Type, Callable, List

from allocation.domain import event, command
from allocation.domain.command import Command
from allocation.domain.event import Event

Message = Union[Event, Command]


class MessageBus:
    def __init__(self,
                 uow,
                 event_handlers: Dict[Type[event.Event], List[Callable]],
                 command_handlers: Dict[Type[command.Command], Callable]
                 ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers

    def handle(self, message: Message):
        results = []
        queue = [message]
        while queue:
            m = queue.pop(0)
            if isinstance(m, Command):
                results.append(self.handle_command(m, queue))
            elif isinstance(m, Event):
                self.handle_event(m, queue)
        return results

    def handle_command(self, cmd: Command, queue: List[Message]):
        handler = self.command_handlers.get(type(cmd), None)
        if not handler:
            raise
        print(f"Handle command {cmd}")
        result = handler(cmd)
        queue.extend(self.uow.collect_new_events())
        return result

    def handle_event(self, e: Event, queue: List[Message]):
        hs = self.event_handlers.get(type(e), None)
        if not hs:
            return

        for h in hs:
            print(f"Handle event: {e}")
            h(e)
            queue.extend(self.uow.collect_new_events())

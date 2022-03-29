import dataclasses
import datetime


class Event:
    def __init__(self, current_time):
        self.current_time = current_time


@dataclasses.dataclass
class MailEvent(Event):
    def __init__(self, message):
        super().__init__(datetime.datetime.today())
        self.message = message


@dataclasses.dataclass
class Allocated:
    orderid: str
    sku: str
    qty: int
    batchref: str


@dataclasses.dataclass
class OutOfStock(Event):
    sku: str


@dataclasses.dataclass
class InvalidBatchRef(Event):
    ref: str

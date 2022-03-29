from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey, event
from sqlalchemy.orm import mapper, relationship

from src.allocation.domain import model

metadata = MetaData()

order_lines = Table(
    'order_lines',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255), ),
    Column('qty', Integer, ),
    Column('orderId', String(255)),
)

batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("ref", String(255)),
    Column("sku", ForeignKey("products.sku", ondelete="CASCADE")),
    Column("_purchased_quantity", Integer, nullable=False),
    Column("eta", Date, nullable=True),
)

products = Table(
    'products',
    metadata,
    Column('sku', String(255), primary_key=True),
    Column('version', Integer, nullable=False, server_default='0')
)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id", ondelete="CASCADE"),),
    Column("batch_id", ForeignKey("batches.id", ondelete="CASCADE")),
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
    batches_mapper = mapper(
        model.Batch,
        batches,
        properties={
            "_allocations": relationship(
                lines_mapper, secondary=allocations, collection_class=set, cascade="all, delete"
            )
        },
    )
    mapper(
        model.Product,
        products,
        properties={
            "batches": relationship(batches_mapper, cascade="all, delete-orphan")
        }
    )


@event.listens_for(model.Product, "load")
def receive_load(product, _):
    product.events = []

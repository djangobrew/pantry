from ninja.orm import create_schema
from ninja import ModelSchema, Schema
from decimal import Decimal

from ep05.models import Order, Item, Barista


BaristaSchema = create_schema(Barista)
ItemSchema = create_schema(Item)
OrderSchema = create_schema(Order)
OrderReadSchema = create_schema(
    model=Order,
    fields=['number', 'barista', 'items', 'datetime'],
    custom_fields=[('total', float, None)],
    depth=1
)


class OrderWriteSchema(Schema):
    barista_id: int
    items: list[int]


class OrderUpdateSchema(Schema):
    items: int | list[int]

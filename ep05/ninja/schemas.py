from ninja.orm import create_schema
from ninja import ModelSchema, Schema
from decimal import Decimal

from pydantic import field_validator

from ep05.models import Order, Item, Barista


BaristaReadSchema = create_schema(Barista)
ItemReadSchema = create_schema(Item)
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


class ItemWriteSchema(Schema):
    name: str
    price: float

    @field_validator('price', mode='after')
    def check_price(cls, value: float) -> float:
        if value <= 0:
            raise ValueError('Price must be greater than $0.00!')
        return value


class BaristaWriteSchema(Schema):
    name: str

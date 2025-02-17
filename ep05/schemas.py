from ninja.orm import create_schema
from ninja import ModelSchema

from ep05.models import Order, Item, Barista


BaristaSchema = create_schema(Barista)
ItemSchema = create_schema(Item)
OrderSchema = create_schema(
    Order,
    fields=['number', 'barista', 'items', 'datetime', 'total'],
    custom_fields=[('total', int)],
    depth=2
)

# class OrderSchema(ModelSchema):
#     total: int

#     class Meta:
#         model = Order
#         fields = ['number', 'barista', 'items', 'datetime', 'total']
#         depth = 2

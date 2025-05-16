from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import NinjaAPI

from ep05.models import Barista, Order, Item
from ep05.ninja.schemas import (
    BaristaReadSchema,
    BaristaWriteSchema,
    ItemReadSchema,
    ItemWriteSchema,
    OrderReadSchema,
    OrderWriteSchema,
    OrderUpdateSchema,
)

api = NinjaAPI(urls_namespace="ep05:ninja")


@api.get('/order', response=OrderReadSchema, tags=["Orders"])
def get_order(request, order_number: int):
    order = get_object_or_404(Order, number=order_number)

    return order


@api.put('/order/{order_number}', response=OrderReadSchema, tags=["Orders"])
def update_order(request, order_number: int, data: OrderUpdateSchema):
    order = get_object_or_404(Order, number=order_number)
    items = data.items

    if isinstance(items, int):
        items = [items]

    order.items.set(items)

    return order


@api.delete('/order/{order_number}', response={204: None}, tags=["Orders"])
def delete_order(request, order_number: int):
    order = get_object_or_404(Order, number=order_number)
    order.delete()

    return 204, None


@api.get('/orders', response=list[OrderReadSchema], tags=["Orders"])
def get_orders(request):
    return Order.objects.all()


@api.post('/orders', response=OrderReadSchema, tags=["Orders"])
def create_order(request, data: OrderWriteSchema):
    order = Order.objects.create(barista_id=data.barista_id)
    order.items.add(*data.items)
    
    return order


@api.get('/items', response=list[ItemReadSchema], tags=["Items"])
def get_items(request):
    return Item.objects.all()


@api.post('/items', response=ItemReadSchema, tags=["Items"])
def create_item(request, data: ItemWriteSchema):
    item = Item.objects.create(name=data.name, price=data.price)
    return item


@api.get('/items/{item_pk}', response=ItemReadSchema, tags=["Items"])
def get_item(request, item_pk: int):
    item = get_object_or_404(Item, pk=item_pk)
    return item


@api.delete('/item/{item_pk}', response={204: None}, tags=["Items"])
def delete_item(request, item_pk: int):
    item = get_object_or_404(Item, pk=item_pk)
    item.delete()

    return 204, None


@api.put('/item/{item_pk}', response=ItemReadSchema, tags=["Items"])
def update_item(request, item_pk, data: ItemWriteSchema):
    item = get_object_or_404(Item, pk=item_pk)
    item.name = data.name
    item.price = data.price
    item.save()

    return item


@api.get('/baristas', response=list[BaristaReadSchema], tags=["Baristas"])
def get_baristas(request):
    return Barista.objects.all()


@api.post('/baristas', response=BaristaReadSchema, tags=["Baristas"])
def create_barista(request, data: BaristaWriteSchema):
    barista = Barista.objects.create(name=data.name)
    return barista


@api.get('/baristas/{barista_pk}', response=BaristaReadSchema, tags=["Baristas"])
def get_barista(request, barista_pk: int):
    barista = get_object_or_404(Barista, pk=barista_pk)
    return barista


@api.put('/baristas/{barista_pk}', response=BaristaReadSchema, tags=["Baristas"])
def update_barista(request, barista_pk: int, data: BaristaWriteSchema):
    barista = get_object_or_404(Barista, pk=barista_pk)
    barista.name = data.name
    barista.save()

    return barista


@api.delete('/baristas/{barista_pk}', response={204: None}, tags=["Baristas"])
def delete_barista(request, barista_pk: int):
    barista = get_object_or_404(Barista, pk=barista_pk)
    barista.delete()

    return 204, None

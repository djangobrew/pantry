from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import NinjaAPI

from ep05.models import Barista, Order, Item
from ep05.ninja.schemas import BaristaSchema, ItemSchema, OrderReadSchema, OrderWriteSchema, OrderUpdateSchema


api = NinjaAPI(urls_namespace="ep05:ninja")


@api.get('/order', response=OrderReadSchema)
def get_order(request, order_number: int):
    order = get_object_or_404(Order, number=order_number)

    return order


@api.put('/order', response=OrderReadSchema)
def update_order(request, order_number: int, data: OrderUpdateSchema):
    order = get_object_or_404(Order, number=order_number)
    items = data.items

    if isinstance(items, int):
        items = [items]

    order.items.set(items)

    return order


@api.delete('/order', response={204: None})
def delete_order(request, order_number: int):
    order = get_object_or_404(Order, number=order_number)
    order.delete()

    return 204, None


@api.get('/orders', response=list[OrderReadSchema])
def get_orders(request):
    return Order.objects.all()


@api.get('/items', response=list[ItemSchema])
def get_items(request):
    return Item.objects.all()


@api.post('/orders', response=OrderReadSchema)
def update_orders(request, data: OrderWriteSchema):
    order = Order.objects.create(barista_id=data.barista_id)
    order.items.add(*data.items)
    
    return order

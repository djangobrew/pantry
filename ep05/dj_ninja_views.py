from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from ep05.schemas import BaristaSchema, OrderSchema, ItemSchema

api = NinjaAPI(urls_namespace="ep05:ninja")


# http://127.0.0.1:8000/ep05/ninja/add?a=1&b=2
@api.get('/add')
def add(request, a: int, b: int):
    return {"result": a + b}


@api.get('/orders')
def orders(request, response=OrderSchema):
    return Order.objects.all()

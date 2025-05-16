from django.shortcuts import get_object_or_404, render

from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ep05.models import Order, Item, Barista
from ep05.drf.serializers import OrderReadSerializer, OrderWriteSerializer, BaristaSerializer, ItemSerializer


class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


@extend_schema(
 description='Order List and Create',
 tags=['Orders']
)
class OrderListCreate(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderReadSerializer,
        'POST': OrderWriteSerializer
    }


@extend_schema(
 description='Order Retrieve, Update, and Destroy',
 tags=['Orders']
)
class OrderRetrieveUpdateDestroy(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = 'number'

    serializer_map = {
        'GET': OrderReadSerializer,
        'DELETE': OrderReadSerializer,
        'PUT': OrderWriteSerializer,
        'PATCH': OrderWriteSerializer,
    }


@extend_schema(
 description='Barista List and Create',
 tags=['Baristas']
)
class BaristaListCreate(generics.ListCreateAPIView):
    queryset = Barista.objects.all()
    serializer_class = BaristaSerializer


@extend_schema(
 description='Barista Retrieve, Update, and Destroy',
 tags=['Baristas']
)
class BaristaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barista.objects.all()
    serializer_class = BaristaSerializer
    lookup_field = 'pk'


@extend_schema(
 description='Item List and Create',
 tags=['Items']
)
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@extend_schema(
 description='Item Retrieve, Update, and Destroy',
 tags=['Items']
)
class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ep05.models import Order, Item, Barista
# from ep05.serializers import OrderSerializer, ItemSerializer, BaristaSerializer
from ep05.serializers import *


# Create your views here.
@api_view()
def drf1(request):
    if request.method == 'POST':
        return Response({'message': 'Got some data', 'data': request.data})
    return Response({'message': 'Hello, World'})


class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class OrderListCreate(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_map = {
        'GET': OrderReadSerializer,
        'POST': OrderWriteSerializer
    }


class OrderRetrieveUpdateDestroy(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = 'number'

    serializer_map = {
        'GET': OrderReadSerializer,
        'DELETE': OrderReadSerializer,
        'PUT': OrderWriteSerializer,
        'PATCH': OrderWriteSerializer,
    }

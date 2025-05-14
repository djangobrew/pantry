from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import JsonResponse

from ep05.models import Order, Item, Barista


def orders(request, *args, **kwargs):
    orders = Order.objects.all()

    return JsonResponse({'orders': serializers.serialize('json', orders)})

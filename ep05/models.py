from functools import partial
import random
from typing import Optional

from django.contrib import admin
from django.db import models


def generate_int(n: int) -> int:
    """ Return an integer of a fixed length. """
    range_start = 10**(n-1)
    range_end = (10**n)-1

    return random.randint(range_start, range_end)


class Item(models.Model):
    name = models.CharField(max_length=50,)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    sku = models.IntegerField(unique=True, default=partial(generate_int, 16))

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


class Barista(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.IntegerField(
        unique=True,
        default=partial(generate_int, 8)
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Order(models.Model):
    number = models.IntegerField(unique=True, default=partial(generate_int, 5))
    items = models.ManyToManyField('Item', related_name='orders')
    datetime = models.DateTimeField(auto_now_add=True)
    barista = models.ForeignKey(
        'Barista',
        null=True,
        on_delete=models.SET_NULL,
        related_name='barista'
    )

    @property
    @admin.display
    def total(self) -> Optional[float]:
        _total = Item.objects.filter(orders__number=self.number).aggregate(price=models.Sum('price'))['price']
        return round(_total, 2) if _total else None

    def __str__(self) -> str:
        return f'{self.number} - total ${self.total}'

from rest_framework import serializers

from ep05.models import Item, Barista, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price']
        read_only_fields = ['sku']


class BaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barista
        fields = ['name']
        read_only_fields = ['employee_id']


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'barista', 'items', 'datetime', 'total']
        read_only_fields = ['number', 'datetime', 'total']
        depth = 2


class OrderWriteSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)
    barista = serializers.PrimaryKeyRelatedField(queryset=Barista.objects.all())

    class Meta:
        model = Order
        fields = ['number', 'barista', 'items', 'datetime', 'total']
        read_only_fields = ['number', 'datetime', 'total']

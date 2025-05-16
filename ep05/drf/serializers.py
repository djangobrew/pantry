from rest_framework import serializers

from ep05.models import Item, Barista, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'sku', 'pk']
        read_only_fields = ['sku', 'pk']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than $0.00!')
        return value


class BaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barista
        fields = ['name', 'employee_id', 'pk']
        read_only_fields = ['employee_id', 'pk']


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

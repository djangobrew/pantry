from django.contrib import admin

from ep05.models import Item, Barista, Order

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['number', 'total']


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ['sku']


class BaristaAdmin(admin.ModelAdmin):
    readonly_fields = ['employee_id']

admin.site.register(Item, ItemAdmin)
admin.site.register(Barista, BaristaAdmin)
admin.site.register(Order, OrderAdmin)

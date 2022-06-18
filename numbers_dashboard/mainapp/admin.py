from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    search_fields = (
        'order_id',
        'usd_price',
        'rur_price',
        'delivery_date',
    )
    list_display = (
        'order_id',
        'usd_price',
        'rur_price',
        'delivery_date',
        'created_at',
        'updated_at',
    )


admin.site.register(Order, OrderAdmin)

from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'usd_price', 'rur_price', 'delivery_date')
        read_only_fields = fields

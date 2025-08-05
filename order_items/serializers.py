from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.product_name')
    order_id = serializers.ReadOnlyField(source='order.order_id')

    class Meta:
        model = OrderItem
        fields = [
            'order_item_id',
            'order_id',
            'product',
            'product_name',
            'order_item_quantity',
            'product_price_at_purchase',
        ]
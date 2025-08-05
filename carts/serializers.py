from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_id', 'user', 'cart_created_at', 'cart_updated_at', 'cart_is_active']
        read_only_fields = ['cart_id', 'cart_created_at', 'cart_updated_at']
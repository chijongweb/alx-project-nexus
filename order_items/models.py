from django.db import models
from orders.models import Order
from products.models import Product

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_quantity = models.PositiveIntegerField(default=1)
    product_price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order_item_quantity} x {self.product.product_name} (Order {self.order.order_id})"
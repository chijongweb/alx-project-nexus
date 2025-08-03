from django.db import models
from carts.models import Cart
from products.models import Product

class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_item_quantity = models.PositiveIntegerField(default=1)
    cart_item_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart_item_quantity} x {self.product.product_name}"
python
Copy
Edit

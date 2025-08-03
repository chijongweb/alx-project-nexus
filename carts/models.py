from django.db import models
from users.models import User

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    cart_created_at = models.DateTimeField(auto_now_add=True)
    cart_updated_at = models.DateTimeField(auto_now=True)
    cart_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart {self.cart_id} - User {self.user.username}"
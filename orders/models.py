from django.db import models
from users.models import User

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_status = models.CharField(max_length=50)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.order_status}"
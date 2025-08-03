from django.db import models
from orders.models import Order

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255, unique=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    payment_paid_at = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.payment_status}"
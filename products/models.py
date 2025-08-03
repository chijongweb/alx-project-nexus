from django.db import models
from categories.models import Category

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_slug = models.SlugField(max_length=255, unique=True)
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
    product_image_url = models.URLField(blank=True)
    is_product_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
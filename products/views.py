from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category__product_name', 'category__category_slug']  # adjust field as needed
    ordering_fields = ['product_price', 'product_created_at']  # fields that can be sorted
    ordering = ['product_created_at']  # default ordering
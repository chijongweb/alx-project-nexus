from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# If using ViewSets and DRF routers (recommended for scalability)
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = router.urls
from django.urls import path
from .views import CartItemListCreateView, CartItemRetrieveUpdateDestroyView

urlpatterns = [
    path('', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('<int:cart_item_id>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cartitem-detail'),
]
from django.urls import path
from .views import CategoryListView  # assuming you have a view here

urlpatterns = [
    # Example endpoint: list categories
    path('', CategoryListView.as_view(), name='category-list'),
]
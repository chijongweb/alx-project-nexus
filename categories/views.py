from django.shortcuts import render
from django.urls import path
from django.http import JsonResponse
from django.views import View

class CategoryListView(View):
    def get(self, request):
        return JsonResponse({"message": "Categories endpoint placeholder"})

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
]
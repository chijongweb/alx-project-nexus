from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer

class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only carts belonging to the logged-in user
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
       
        serializer.save(user=self.request.user)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow access to carts owned by the logged-in user
        return Cart.objects.filter(user=self.request.user)
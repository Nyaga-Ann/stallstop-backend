from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)


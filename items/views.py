from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, permissions
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ItemFilter
    search_fields = ["name", "description", "vendor__business_name"]
    ordering_fields = ["price", "created_at"]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsVendorOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)



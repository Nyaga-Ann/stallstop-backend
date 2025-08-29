from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, permissions
from .models import Item, ItemFavorite
from .serializers import ItemSerializer, ItemFavoriteSerializer
from .permissions import IsVendorOwnerOrReadOnly 
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

class MyItemFavoritesView(generics.ListCreateAPIView):
    serializer_class = ItemFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemFavorite.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class ItemFavoriteDetailView(generics.DestroyAPIView):
    serializer_class = ItemFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItemFavorite.objects.filter(customer=self.request.user)

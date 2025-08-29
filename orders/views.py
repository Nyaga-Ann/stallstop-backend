from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOrderCustomer, IsOrderVendor
from items.models import Item

class CustomerOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        item_id = self.request.data.get("item")
        item = Item.objects.select_related("vendor").get(pk=item_id)
        serializer.save(
            customer=self.request.user,
            vendor=item.vendor
        )

class CustomerOrderDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderCustomer]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class VendorIncomingOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(vendor__user=self.request.user)

class VendorOrderStatusUpdateView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderVendor]
    queryset = Order.objects.all()
    http_method_names = ["patch", "put"]

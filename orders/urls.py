from django.urls import path
from .views import (
    CustomerOrderListCreateView, CustomerOrderDetailView,
    VendorIncomingOrdersView, VendorOrderStatusUpdateView
)

urlpatterns = [
    # customer
    path("me/", CustomerOrderListCreateView.as_view(), name="customer-orders"),
    path("me/<int:pk>/", CustomerOrderDetailView.as_view(), name="customer-order-detail"),
    # vendor
    path("vendor/", VendorIncomingOrdersView.as_view(), name="vendor-incoming-orders"),
    path("<int:pk>/status/", VendorOrderStatusUpdateView.as_view(), name="vendor-order-status"),
]

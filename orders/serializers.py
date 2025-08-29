from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source="item.name", read_only=True)
    vendor_name = serializers.CharField(source="vendor.business_name", read_only=True)
    customer_username = serializers.CharField(source="customer.username", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "item", "item_name", "vendor", "vendor_name", "customer", "customer_username",
                  "quantity", "status", "note", "created_at"]
        read_only_fields = ["id", "customer", "status", "created_at", "vendor"]

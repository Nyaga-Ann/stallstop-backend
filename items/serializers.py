from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source="vendor.business_name", read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "vendor",
            "vendor_name",
            "name",
            "category",
            "price",
            "description",
            "image_url",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "vendor"]

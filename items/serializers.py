from rest_framework import serializers
from .models import Item, ItemFavorite
from vendors.models import VendorProfile

class VendorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ["id", "business_name", "shop_type", "location"]

class ItemSerializer(serializers.ModelSerializer):
    vendor = VendorMiniSerializer(read_only=True)
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

class ItemFavoriteSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source="item.name", read_only=True)

    class Meta:
        model = ItemFavorite
        fields = ["id", "item", "item_name", "created_at"]
        read_only_fields = ["id", "created_at"]

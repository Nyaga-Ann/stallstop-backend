from rest_framework import serializers
from .models import VendorProfile, VendorFavorite

class VendorProfileSerializer(serializers.ModelSerializer):
    whatsapp_link = serializers.SerializerMethodField()

    class Meta:
        model = VendorProfile
        fields = [
            "id", "business_name", "location", "latitude", "longitude",
            "description", "contact_phone", "shop_type",
            "whatsapp_number", "whatsapp_link"
        ]

    def get_whatsapp_link(self, obj):
        if obj.whatsapp_number:
            return f"https://wa.me/{obj.whatsapp_number}"
        return None

class VendorFavoriteSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source="vendor.business_name", read_only=True)

    class Meta:
        model = VendorFavorite
        fields = ["id", "vendor", "vendor_name", "created_at"]
        read_only_fields = ["id", "created_at"]
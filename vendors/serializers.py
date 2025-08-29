from rest_framework import serializers
from .models import VendorProfile

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

from rest_framework import serializers
from .models import VendorProfile, VendorFavorite, VendorReview
from django.db.models import Avg

class VendorProfileSerializer(serializers.ModelSerializer):
    whatsapp_link = serializers.SerializerMethodField()
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = VendorProfile
        fields = [
            "id", "business_name", "location", "latitude", "longitude",
            "description", "contact_phone", "shop_type",
            "whatsapp_number", "whatsapp_link", "avg_rating"
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

class VendorReviewSerializer(serializers.ModelSerializer):
    customer_username = serializers.CharField(source="customer.username", read_only=True)

    class Meta:
        model = VendorReview
        fields = ["id", "vendor", "customer", "customer_username", "rating", "comment", "created_at"]
        read_only_fields = ["id", "customer", "created_at"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
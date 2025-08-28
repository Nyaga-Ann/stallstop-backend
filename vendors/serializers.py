from rest_framework import serializers
from .models import VendorProfile

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = "__all__"
        read_only_fields = ["user"]

from django.contrib import admin
from .models import VendorProfile

@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "business_name", "location", "shop_type", "contact_phone")
    search_fields = ("business_name", "location")
    list_filter = ("shop_type",)


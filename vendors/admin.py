from django.contrib import admin
from .models import VendorProfile, VendorReview, VendorFavorite

@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "business_name", "location", "shop_type", "contact_phone")
    search_fields = ("business_name", "location")
    list_filter = ("shop_type",)

@admin.register(VendorReview)
class VendorReviewAdmin(admin.ModelAdmin):
    list_display = ("vendor", "customer", "rating", "created_at")
    search_fields = ("vendor__business_name", "customer__username")

@admin.register(VendorFavorite)
class VendorFavoriteAdmin(admin.ModelAdmin):
    list_display = ("vendor", "customer", "created_at")
    search_fields = ("vendor__business_name", "customer__username")
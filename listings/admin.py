from django.contrib import admin
from .models import ItemListing

@admin.register(ItemListing)
class ItemListingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "location", "vendor", "created_at")
    search_fields = ("name", "category", "location", "vendor__business_name")
    list_filter = ("category",)

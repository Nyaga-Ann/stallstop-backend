from django.contrib import admin
from .models import Item, ItemFavorite


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "vendor", "created_at")
    list_filter = ("category", "vendor")
    search_fields = ("name", "vendor__business_name")


@admin.register(ItemFavorite)
class ItemFavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "item", "created_at")
    list_filter = ("created_at", "customer")
    search_fields = ("customer__username", "item__name")

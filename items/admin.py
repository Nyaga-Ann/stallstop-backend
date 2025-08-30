from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "vendor", "price", "stock", "created_at")
    list_filter = ("vendor",)
    search_fields = ("name", "vendor__shop_name")

@admin.register(ItemFavorite)
class ItemFavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "created_at")
    search_fields = ("user__username", "item__name")
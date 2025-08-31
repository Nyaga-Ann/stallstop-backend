from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "get_items", "total_price", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username",)

    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    get_items.short_description = "Items"



from django.db import models
from vendors.models import VendorProfile

class Item(models.Model):
    class Category(models.TextChoices):
        CLOTHING = "clothing", "Clothing"
        SHOES = "shoes", "Shoes"
        ACCESSORIES = "accessories", "Accessories"

    vendor = models.ForeignKey(
        VendorProfile,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=Category.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)      
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.vendor.business_name}"

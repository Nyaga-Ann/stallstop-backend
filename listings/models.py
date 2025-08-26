from django.db import models
from vendors.models import VendorProfile

class ItemListing(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=60)  # optional: later migrate to FK Category
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=120)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}"

from django.db import models
from django.conf import settings

class VendorProfile(models.Model):
    class ShopType(models.TextChoices):
        PHYSICAL = "physical", "Physical"
        DIGITAL = "digital", "Digital"
        BOTH = "both", "Both"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor_profile"
    )
    business_name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)  # e.g., "Nairobi CBD"
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField(blank=True)
    contact_phone = models.CharField(max_length=30)
    shop_type = models.CharField(max_length=10, choices=ShopType.choices, default=ShopType.PHYSICAL)
    whatsapp_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.business_name} - {self.location}"

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

class VendorFavorite(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorite_vendors")
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("customer", "vendor")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer} ⭐ {self.vendor}"

class VendorReview(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor_reviews")
    rating = models.PositiveSmallIntegerField()  # 1..5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("vendor", "customer")  # one review per customer per vendor

    def __str__(self):
        return f"{self.vendor} rated {self.rating} by {self.customer}"

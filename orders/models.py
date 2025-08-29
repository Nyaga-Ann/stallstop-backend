from django.db import models
from django.conf import settings
from items.models import Item
from vendors.models import VendorProfile

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orders")
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name="orders")
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.id} - {self.item.name} x{self.quantity}"
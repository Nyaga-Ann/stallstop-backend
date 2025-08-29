from django.urls import path
from .views import MyCustomerProfileView

urlpatterns = [
    path("me/", MyCustomerProfileView.as_view(), name="customer-me"),
]

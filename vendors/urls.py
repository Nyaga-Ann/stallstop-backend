from django.urls import path
from . import views

urlpatterns = [
    path("", views.VendorListCreateView.as_view(), name="vendor-list-create"),
    path("<int:pk>/", views.VendorDetailView.as_view(), name="vendor-detail"),
]

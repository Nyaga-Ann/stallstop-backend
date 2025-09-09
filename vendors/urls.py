from django.urls import path
from . import views
from .views import MyVendorFavoritesView, VendorFavoriteDetailView, VendorReviewListCreateView, VendorReviewDetailView, MyVendorProfileView

urlpatterns = [
    path("", views.VendorListCreateView.as_view(), name="vendor-list-create"),
    path("<int:pk>/", views.VendorDetailView.as_view(), name="vendor-detail"),
    path("me/", MyVendorProfileView.as_view(), name="my-vendor-profile"),
    path("favorites/", MyVendorFavoritesView.as_view(), name="my-vendor-favorites"),
    path("favorites/<int:pk>/", VendorFavoriteDetailView.as_view(), name="vendor-favorite-detail"),
    path("<int:vendor_id>/reviews/", VendorReviewListCreateView.as_view(), name="vendor-review-list"),
    path("<int:vendor_id>/reviews/<int:pk>/", VendorReviewDetailView.as_view(), name="vendor-review-detail"),
]

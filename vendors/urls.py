from django.urls import path
from . import views
from .views import MyVendorFavoritesView, VendorFavoriteDetailView

urlpatterns = [
    path("", views.VendorListCreateView.as_view(), name="vendor-list-create"),
    path("<int:pk>/", views.VendorDetailView.as_view(), name="vendor-detail"),
    path("favorites/", MyVendorFavoritesView.as_view(), name="my-vendor-favorites"),
    path("favorites/<int:pk>/", VendorFavoriteDetailView.as_view(), name="vendor-favorite-detail"),
]

from django.urls import path
from . import views
from .views import MyItemFavoritesView, ItemFavoriteDetailView

urlpatterns = [
    path("", views.ItemListCreateView.as_view(), name="item-list"),
    path("<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),
     path("favorites/", MyItemFavoritesView.as_view(), name="my-item-favorites"),
    path("favorites/<int:pk>/", ItemFavoriteDetailView.as_view(), name="item-favorite-detail"),
]

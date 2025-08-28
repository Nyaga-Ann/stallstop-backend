from django.urls import path
from . import views

urlpatterns = [
    path("", views.ItemListCreateView.as_view(), name="item-list-create"),
    path("<int:pk>/", views.ItemDetailView.as_view(), name="item-detail"),
]
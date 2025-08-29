from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.http import JsonResponse

def root(_):
    return JsonResponse({"service": "StallStop API", "status": "ok"})

urlpatterns = [
    path("", root, name="root"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),

    # App URLs
    path("api/users/", include("users.urls")),
    path("api/vendors/", include("vendors.urls")),
    path("api/items/", include("items.urls")),
    path("api/customers/", include("customers.urls")),

    # API schema & docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

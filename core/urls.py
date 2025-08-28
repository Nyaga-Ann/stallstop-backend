from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

def root(_):
    return JsonResponse({"service": "StallStop API", "status": "ok"})

schema_view = get_schema_view(
    openapi.Info(
        title="StallStop API",
        default_version="v1",
        description="Vendor Directory API for fashion listings (StallStop)",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("", root, name="root"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),

    # App URLs
    path("api/users/", include("users.urls")),
    path("api/vendors/", include("vendors.urls")),
    path("api/items/", include("items.urls")),


    # Docs
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

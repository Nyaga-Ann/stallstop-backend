from django.urls import path
from django.http import JsonResponse

def health(_):
    return JsonResponse({"status": "ok", "service": "listings"})

urlpatterns = [
    path("health/", health, name="listings-health"),
]


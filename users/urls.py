from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerLoginView, VendorLoginView

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("customer/signup/", CustomerSignupView.as_view(), name="customer-signup"),
    path("vendor/signup/", VendorSignupView.as_view(), name="vendor-signup"),
    path("customer/login/", CustomerLoginView.as_view(), name="customer-login"),
    path("vendor/login/", VendorLoginView.as_view(), name="vendor-login"),
]



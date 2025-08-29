from django.shortcuts import render
from django.db.models import Avg
from rest_framework import generics, permissions, viewsets
from .models import VendorProfile, VendorFavorite, VendorReview
from .serializers import VendorProfileSerializer, VendorFavoriteSerializer, VendorReviewSerializer
from .permissions import IsVendorOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = VendorProfile.objects.all().annotate(avg_rating=Avg("reviews__rating"))
    serializer_class = VendorProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VendorProfileViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsVendorOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyVendorFavoritesView(generics.ListCreateAPIView):
    serializer_class = VendorFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VendorFavorite.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class VendorFavoriteDetailView(generics.DestroyAPIView):
    serializer_class = VendorFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VendorFavorite.objects.filter(customer=self.request.user)

class VendorReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = VendorReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        vendor_id = self.kwargs["vendor_id"]
        return VendorReview.objects.filter(vendor_id=vendor_id)

    def perform_create(self, serializer):
        vendor_id = self.kwargs["vendor_id"]
        serializer.save(customer=self.request.user, vendor_id=vendor_id)

class VendorReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_id = self.kwargs["vendor_id"]
        # only author can update/delete
        return VendorReview.objects.filter(vendor_id=vendor_id, customer=self.request.user)
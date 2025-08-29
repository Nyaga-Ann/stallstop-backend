from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import VendorProfile
from .serializers import VendorSerializer
from .permissions import IsVendorOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VendorProfileViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsVendorOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


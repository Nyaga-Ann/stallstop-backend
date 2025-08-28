from django.shortcuts import render
from rest_framework import generics, permissions
from .models import VendorProfile
from .serializers import VendorSerializer

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


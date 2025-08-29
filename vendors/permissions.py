from rest_framework import permissions

class IsVendorOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods: allow GET for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, only vendor owner can modify
        return obj.user == request.user

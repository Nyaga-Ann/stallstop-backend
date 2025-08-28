from rest_framework import permissions

class IsVendorOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only vendor owners can update/delete their own items.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE METHODS (GET, HEAD, OPTIONS) are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the owner vendor can modify
        return obj.vendor.user == request.user

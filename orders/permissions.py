from rest_framework import permissions

class IsOrderCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

class IsOrderVendor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.vendor.user == request.user

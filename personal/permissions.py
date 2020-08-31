from rest_framework.permissions import BasePermission


class CanConfirmOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class CanCompleteOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # print("user::", request.user)
        return bool(request.method in permissions.SAFE_METHODS) or bool(request.user and request.user.is_staff)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print("user::", request.user.username)
        # print("user obj::", obj.user.username)
        return request.user == obj.user

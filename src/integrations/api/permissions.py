from django.conf import settings
from rest_framework import permissions

class PermissionSlugIsMissing(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.kwargs.get("warehouse") in settings.SLUGS
    
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """ Allows access only to admin users"""
    def has_permission(self, request, view):

    	if request.method in permissions.SAFE_METHODS:
    		return True
    	return request.user and request.user.is_staff
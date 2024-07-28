from rest_framework import permissions #type: ignore

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permission class to allow users to edit their own profile,
    while allowing GET and POST requests for all users.

    Attributes:
        - SAFE_METHODS: Tuple of HTTP methods (GET, HEAD, OPTIONS) considered safe.

    Methods:
        - has_permission(self, request, view):
            Returns whether the user is allowed to perform the action based on request method.

        - has_object_permission(self, request, view, obj):
            Returns whether the user has permission to access or modify a specific object.
    """

    def has_permission(self, request, view):
        """
        Check if the user is the owner of the profile or if the request method is safe.

        Args:
            request: HTTP request object.
            view: The view requesting the permission check.

        Returns:
            bool: True if permission is granted, False otherwise.
        """
        return True
    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the profile or if the request method is safe.

        Args:
            request: HTTP request object.
            view: The view requesting the permission check.
            obj: The object being accessed or modified.

        Returns:
            bool: True if permission is granted, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow POST requests for anonymous users
        if not request.user.is_anonymous:
            return True

        return False

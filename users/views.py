from django.contrib.auth.models import User

from rest_framework import viewsets #type: ignore

from .serializers import UserSerializer

from .permissions import IsUserOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    permission_classes = [IsUserOwnerOrGetAndPostOnly]  # Custom permission class for user permissions.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


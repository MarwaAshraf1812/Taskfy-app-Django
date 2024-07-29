"""
URL configuration for Taskfy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from users import routers as users_api_router

# Initialize an empty list to store authentication-related URL patterns
auth_url_patterns = [
    path('', include('rest_framework_social_oauth2.urls')),
]

# If DEBUG mode is enabled in Django settings
if settings.DEBUG:
    # Add Django Rest Framework's built-in authentication URLs
    # This includes login and logout views, which are useful for testing in development
    auth_url_patterns.append(path(r'verify/', include('rest_framework.urls')))

api_url_patterns = [
    path('auth/', include(auth_url_patterns)),
    path('accounts/', include(users_api_router.router.urls)),
]
urlpatterns = [
    # Include the authentication URL patterns under the 'auth/' prefix
    # This creates URLs like /api/auth/verify/login/ and /api/auth/verify/logout/
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
]

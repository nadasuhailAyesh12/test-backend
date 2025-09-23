"""
URL patterns for user management.
"""
from rest_framework.routers import DefaultRouter
from .views import UserViewSet #UserProfileViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


urlpatterns = router.urls

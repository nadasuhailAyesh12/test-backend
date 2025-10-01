from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, AssignmentSubmissionViewSet

router = DefaultRouter()
router.register('assignments', AssignmentViewSet)
router.register('submissions', AssignmentSubmissionViewSet)

urlpatterns = router.urls

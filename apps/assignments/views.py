from django.shortcuts import render

from rest_framework import viewsets
from .models import Assignment, AssignmentSubmission
from .serializers import AssignmentSerializer, AssignmentSubmissionSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'teacher':
            return AssignmentSubmission.objects.filter(
                assignment__lecture__teacher__user=user
            )
        elif user.role == 'student':
            return AssignmentSubmission.objects.filter(student=user)
        return AssignmentSubmission.objects.none()

    def perform_update(self, serializer):
        user = self.request.user
        submission = self.get_object()

        # تأكدي إن المعلم هو صاحب المحاضرة
        if user.role == 'teacher' and submission.assignment.lecture.teacher.user == user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to grade this submission.")


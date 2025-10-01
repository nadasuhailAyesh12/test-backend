from rest_framework import serializers
from .models import Assignment, AssignmentSubmission

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['assignment', 'student', 'file_url', 'submitted_at', 'grade']
        read_only_fields = ['submitted_at', 'grade']

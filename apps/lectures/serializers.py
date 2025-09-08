from rest_framework import serializers
from .models import Lecture, Teacher
from django.shortcuts import get_object_or_404

class LectureSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'description', 'video', 'pdf','teacher_name']
        extra_kwargs = {'teacher': {'read_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError("Please log in to continue.") 
            
        teacher = Teacher.objects.get(user=user)
        validated_data['teacher'] = teacher
        return super().create(validated_data)

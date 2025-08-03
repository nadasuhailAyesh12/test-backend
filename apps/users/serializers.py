"""
Serializers for user models.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'full_name',
            'date_of_birth', 'profile_picture', 'native_language',
            'learning_level', 'created_at', 'updated_at',
            'email_verified'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'email_verified']


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new users."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'password',
            'password_confirm', 'date_of_birth', 'native_language',
            'learning_level'
        ]

    def validate(self, attrs):
        """Validate password confirmation."""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        """Create user with hashed password."""
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user information."""

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'date_of_birth',
            'profile_picture', 'native_language', 'learning_level'
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'total_study_time', 'lessons_completed',
            'exercises_completed', 'current_streak', 'longest_streak',
            'daily_goal_minutes', 'notifications_enabled',
            'email_notifications', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user', 'total_study_time', 'lessons_completed',
            'exercises_completed', 'current_streak', 'longest_streak',
            'created_at', 'updated_at'
        ]


class PasswordChangeSerializer(serializers.Serializer):
    """Serializer for password change."""

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password]
    )
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        """Validate password confirmation."""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError(
                {"new_password": "Password fields didn't match."}
            )
        return attrs

    def validate_old_password(self, value):
        """Validate old password."""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value
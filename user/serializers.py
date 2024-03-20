from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from cloudinary.models import CloudinaryField
from allauth.account.adapter import get_adapter
from django.core.exceptions import ValidationError
from allauth.account.utils import setup_user_email
from cloudinary.uploader import upload


class UserRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.ImageField()

    def get_cleaned_data(self):
        print(self.validated_data)
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'avatar': self.validated_data.get('avatar')
        }

    def save(self, request):
        # Delegate user creation and password handling to RegisterSerializer
        user = super().save(request)

        # Handle avatar upload (if provided) after user creation
        if self.cleaned_data.get('avatar'):
            try:
                response = upload(
                    self.cleaned_data['avatar'])
                user.avatar = response['url']
                user.save()  # Save the user with the updated avatar URL
            except Exception as e:
                # Provide informative error message
                raise serializers.ValidationError({'avatar': [str(e)]})

        return user

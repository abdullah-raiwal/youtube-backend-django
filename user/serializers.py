from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from cloudinary.models import CloudinaryField
from allauth.account.adapter import get_adapter
from django.core.exceptions import ValidationError
from allauth.account.utils import setup_user_email


# class UserSerializer(RegisterSerializer):
#     # avatar = serializers.ImageField()
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)


#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name',
#                   'last_name', 'password']

#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'min_length': 5
#             }}

#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'password2': self.validated_data.get('password2', ''),
#             'email': self.validated_data.get('email', ''),
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             # 'avatar': self.validated_data.get('avatar', ''),
#         }

 

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         user = adapter.save_user(request, user, self, commit=False)
#         if "password" in self.cleaned_data:
#             try:
#                 adapter.clean_password(self.cleaned_data['password'], user=user)
#             except ValidationError as exc:
#                 raise serializers.ValidationError(
#                     detail=serializers.as_serializer_error(exc)
#                 )
#         user.save()
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         return user

class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        }



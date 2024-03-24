from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from cloudinary.uploader import upload


class UserRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.ImageField(use_url = True)

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
        user = super().save(request)

        if self.cleaned_data.get('avatar'):
            try:
                response = upload(
                    self.cleaned_data['avatar'])
                user.avatar = response['url']
                user.save()
            except Exception as e:
                raise serializers.ValidationError({'avatar': [str(e)]})

        return user

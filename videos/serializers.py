from rest_framework import serializers
from cloudinary.uploader import upload_large, upload
from core.models import Video
from cloudinary.exceptions import GeneralError
from dj_rest_auth.serializers import UserDetailsSerializer


class VideoSerializer(serializers.ModelSerializer):
    videoFile = serializers.FileField()
    thumbnailFile = serializers.ImageField(read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'videoFile', 'title', 'description',
                  'thumbnailFile', 'duration', 'createdAt', 'updatedAt')

        read_only_fields = ('id', 'thumbnailFile', 'duration')

    def get_owner(self, obj):
        return obj.owner.username

    def upload_video(self, file):
        print()
        try:
            results = upload_large(file, resource_type="video")
            return results
        except:
            raise GeneralError('server error')

    def create(self, validated_data):

        response = self.upload_video(self.validated_data['videoFile'])
        print(response)

        validated_data['videoFile'] = response['url']
        validated_data['duration'] = response['duration']
        validated_data['thumbnailFile'] = response['url'].replace(
            '.mp4', '.jpg')
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

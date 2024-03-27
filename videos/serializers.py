from rest_framework import serializers
from cloudinary.uploader import upload_large, upload, destroy
from core.models import Video
from cloudinary.exceptions import GeneralError
from utils.CloudinaryUtils import extract_public_id


class VideoSerializer(serializers.ModelSerializer):
    videoFile = serializers.FileField()
    thumbnailFile = serializers.ImageField(read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'videoFile', 'title', 'description',
                  'thumbnailFile', 'duration', 'createdAt', 'updatedAt')

        read_only_fields = ('id', 'thumbnailFile', 'duration')

    def upload_video(self, file):
        print()
        try:
            results = upload_large(file, resource_type="video")
            return results
        except:
            raise GeneralError('server error')

    def delete_video(self, file_url):
        print(file_url)
        try:

            results = destroy(file_url)
            return results
        except:
            raise GeneralError('server error')

    def create(self,  validated_data):

        response = self.upload_video(self.validated_data['videoFile'])
        print(response)

        validated_data['videoFile'] = response['url']
        validated_data['duration'] = response['duration']
        validated_data['thumbnailFile'] = response['url'].replace(
            '.mp4', '.jpg')
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance,  validated_data):

        if 'videoFile' in validated_data.keys():
            new_video = self.upload_video(validated_data['videoFile'])
            # print( 'instance ->')
            id = extract_public_id(str(instance.videoFile))
            print(id)
            old_video = self.delete_video(id)
            print(old_video)
            validated_data['videoFile'] = new_video['url']

        return super().update(instance, validated_data)

from rest_framework import viewsets
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated
from core.models import Video
from cloudinary.uploader import destroy
from cloudinary.exceptions import GeneralError
from utils.CloudinaryUtils import extract_public_id


class VideoView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(owner=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data['videoFile'])

        try:
            id = extract_public_id(serializer.data['videoFile'])
            print( 'public_id =>',  id)

            destroy(public_id=id, resource_type='video')
        except:
            raise GeneralError('something went wrong. try again later')

        return super().destroy(request, *args, **kwargs)



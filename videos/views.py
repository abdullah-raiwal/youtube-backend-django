from rest_framework import viewsets
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated
from core.models import Video


class VideoView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(owner=self.request.user.id)

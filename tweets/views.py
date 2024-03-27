from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Tweet
from .serializers import TweetSerializer
from rest_framework.response import Response

class tweetViews(viewsets.ModelViewSet):

    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tweet.objects.filter(owner=self.request.user.id)

    
    def destroy(self, request, *args, **kwargs):
         super().destroy(request, *args, **kwargs)
         return Response('deleted')
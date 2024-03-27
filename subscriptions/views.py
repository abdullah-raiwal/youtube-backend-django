from rest_framework import generics
from .serializers import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class createSubscriptionView(generics.CreateAPIView):
    # view to subscribe to a channel
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        channelId = kwargs.get('channelId')
        
        
        return super().post(request, *args, **kwargs)
    
    
    

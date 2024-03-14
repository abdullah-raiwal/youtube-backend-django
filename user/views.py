from rest_framework import generics
from .serializers import UserSerializer

class userCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    

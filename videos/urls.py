from rest_framework.routers import DefaultRouter
from .views import VideoView

videoRouter = DefaultRouter()
videoRouter.register('videos', VideoView, basename='video')

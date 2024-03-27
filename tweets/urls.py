from rest_framework.routers import DefaultRouter
from .views import tweetViews

tweetRouter = DefaultRouter()
tweetRouter.register('tweets', tweetViews, basename='tweets')


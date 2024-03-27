from django.contrib import admin
from django.urls import path, include
from videos.urls import videoRouter
from tweets.urls import tweetRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/', include(videoRouter.urls)),
    path('api/', include(tweetRouter.urls)),
    path('api/', include('subscriptions.urls')),
    # api docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]

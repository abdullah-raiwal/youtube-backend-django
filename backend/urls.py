from django.contrib import admin
from django.urls import path, include
from videos.urls import videoRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/user/', include('user.urls')),
    # api docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include(videoRouter.urls))
]

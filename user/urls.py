from django.urls import path
from .views import userCreateView

app_name = 'user'

urlpatterns = [
    path('register/', userCreateView.as_view(), name='create'),
]

from django.urls import path, include
from .views import createSubscriptionView

urlpatterns = [
    path('subscribe/', createSubscriptionView.as_view(), name='subscribe')
]
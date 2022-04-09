from unicodedata import name
from django.urls import URLPattern, path
from users.api.api import UserAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(),name='usuario_api')
]
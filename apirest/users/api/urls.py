from django.urls import path
from users.api.api import user_api_view

urlpatterns = [
    path('users', user_api_view, name='usuario_api')
]
from django.urls import path
from apps.users.api.api import user_api_view #UserAPIView

urlpatterns = [
    #path('usuario/', UserAPIView.as_view(), name = 'usuario_api')
    path('usuario/', user_api_view, name = 'usuario_api')
]

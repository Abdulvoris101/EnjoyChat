from django.urls import path
from .consumers import PersonalChatConsumer

websocket_urlpatterns = [
    path('chat/<int:id>/', PersonalChatConsumer.as_asgi())
]
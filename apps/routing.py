from django.urls import path

from apps.consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws", ChatConsumer.as_asgi()),
]

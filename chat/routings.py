from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/chat/<int:conversation_id>/', consumers.ChatConsumer.as_asgi()),
]


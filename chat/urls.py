from django.urls import path
from .views import MessageListCreateAPIViews

urlpatterns = [
    path('messages/', MessageListCreateAPIViews.as_view(), name='message-list-create'),
]
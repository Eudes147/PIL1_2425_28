from django.urls import path
from .views import MessageListCreateAPIViews
from.views import chat_view

urlpatterns = [
    path('messages/', MessageListCreateAPIViews.as_view(), name='message-list-create'),
    path('', chat_view, name='chat'),

]

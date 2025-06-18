from django.urls import path
from . import views

urlpatterns = [
    path('conversations/', views.ConversationListView.as_view(), name='conversation_list'),
    path('conversations/<int:pk>/', views.ConversationDetailView.as_view(), name='conversation_detail'),
    path('messages/', views.MessageCreateView.as_view(), name='message_create'),
    path('chat', views.chat_view, name='chat'), 
    path('conversation', views.conversation, name='conversation'),
]
from django.urls import path
from . import views

app_name = "chatting"

urlpatterns = [
    path('chatting_test/', views.chatting_test_view, name='chatting_test'),
    path('chat/<int:user_id>/', views.private_chat_room, name='private_chat_room'),
]

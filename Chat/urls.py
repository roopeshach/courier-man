from django.urls import path
from .import views
urlpatterns = [
    path('chat/<int:id>', views.chat, name='chat'),
    path('users-chat', views.users_chat, name='users-chat'),
]
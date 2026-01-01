from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats, name='chats'),
    path("send/", views.send_message, name="chats_send"),
    path("poll/", views.poll_messages, name="chats_poll"),
]

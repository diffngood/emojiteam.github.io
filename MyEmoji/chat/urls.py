# chat/urls.py

from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', chat, name='chat'),
#     path('<str:room_name>/', room, name='room')
# ]

from chat import views
# URL Reverse시의 namespace로서 활용
app_name = "chat"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_pk>/chat/", views.room_chat, name="room_chat"),
    path("new/", views.room_new, name="room_new"),
]
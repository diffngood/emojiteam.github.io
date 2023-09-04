# emo_create/urls.py

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', page, name='page'),
]

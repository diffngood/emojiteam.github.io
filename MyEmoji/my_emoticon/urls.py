# emo_create/urls.py

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', page, name='page'),
    path('download_image_0/', download_image_0, name='download_image_0'),
    path('download_image_1/', download_image_1, name='download_image_1'),
    path('download_image_2/', download_image_2, name='download_image_2'),
    path('download_image_3/', download_image_3, name='download_image_3'),
    path('download_image_4/', download_image_4, name='download_image_4'),
]

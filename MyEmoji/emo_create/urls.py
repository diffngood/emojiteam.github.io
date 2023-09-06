# emo_create/urls.py

from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', guide, name='guide'),
    path('upload_img/', upload_img, name='upload_img'),
    path('webcam/', webcam, name='webcam'),
    path('detail/<int:pk>', detail, name='detail'),
    path('process_style/', process_style, name='process_style'),
    path('download_image/', download_image, name='download_image'),
    path('loading/', loading, name='loading'),
    path('add_text_to_image/', add_text_to_image, name='add_text_to_image'),
]

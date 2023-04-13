from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', photo, name="photo"),
    path('create/', photoCreate, name="photo_create"),
    path('detail/<int:pk>/', photoDetail, name="photo_detail"),
    path('delete/<int:pk>/', photoDelete, name="photo_delete"),
    path('edit/<int:pk>/', photoEdit, name="photo_edit"),
    path('search/', photolsearchResult, name="photo_search"),
]
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('', photo, name="photo"),
    path('create/', photoCreate, name="photo_create"),
    path('detail/<int:pk>/', photoDetail, name="photo_detail"),
    path('delete/<int:pk>/', photoDelete, name="photo_delete"),
    path('edit/<int:pk>/', photoEdit, name="photo_edit"),
    path('search/', photolsearchResult, name="photo_search"),
]
=======
    path('', board, name='board'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
]
>>>>>>> cdb81bf9dfea302e2301f755250ae452be11be4f

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import *
from .models import *

def photo(request):
    photo = Photo.objects.all().order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(photo, '12')
    page_obj = paginator.get_page(page)
    context = {
        'photo': photo,
        'page_obj': page_obj,
    }
    return render(request, 'photo.html', context)

def photoCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["images"]
        user = request.user
        photo = Photo(
            title=title,
            content=content,
            user=user,
            imgfile=img,
        )
        photo.save()
        return redirect('photo')
    else:
        photoForm = PhotoForm
        context = {
            'photoForm': photoForm,
        }
        return render(request, 'photo_create.html', context)

def photoDetail(request, pk):
    photo_detail = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo_detail.html', {'photo_detail': photo_detail})

def photoEdit(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.title = request.POST['title']
        photo.content = request.POST['content']
        photo.user = request.user
        photo.save()
        return redirect('photo')
    else:
        photoForm = PhotoForm
        return render(request, 'photo_edit.html', {'photoForm':photoForm, 'photo': photo})

def photoDelete(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('photo')

def photolsearchResult(request):
    photos = None
    query = None
    if 'search_photo' in request.GET:
        query = request.GET.get('search_photo')
        photos = Photo.objects.all().filter(Q(title=query) | Q(title__contains=query) | Q(content=query) | Q(content__contains=query)).order_by('-pk')
        page = request.GET.get('page', '1')
        paginator = Paginator(photos, '12')
        page_obj = paginator.page(page)
        return render(request, 'photo_search.html', {'query': query, 'photos': photos, 'page_obj': page_obj})
    else:
        return render(request, 'photo_search.html', {'query': query, 'photos': photos})

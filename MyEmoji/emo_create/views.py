from django.shortcuts import render, redirect
from .models import Img, CameraImage
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def guide(request):
    return render(request, 'guide.html')


def upload_img(request):
    if request.method == "POST":
        post = Img()
        post.date = timezone.now()
        post.image = request.FILES['image']
        post.save()
        return redirect('/emo_create/detail/'+str(post.id), {'post': post})
    else:
        post = Img()
        return render(request, 'upload_img.html', {'post': post})


# def upload_img(request):
#     if request.method == 'POST':
#         form = ImgForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'upload_img.html', {'form': form})
#     else:
#         form = ImgForm()
#     return render(request, 'upload_img.html', {'form': form})


def success(request):
    return HttpResponse('Image Uploaded Successfully')


@csrf_exempt
def webcam(request):
    if request.method == 'POST':
        image = request.FILES.get('camera-image')
        CameraImage.objects.create(image=image)
    images = CameraImage.objects.all()
    context = {
        'images': images
    }
    return render(request, 'webcam.html', context)


def detail(request, pk):
    img = Img.objects.get(id=pk)
    return render(request, 'detail.html', {'img': img})

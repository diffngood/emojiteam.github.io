# import cv2
# from django.http import StreamingHttpResponse
# from django.views.decorators import gzip
from django.shortcuts import render, redirect
from .models import Img, CameraImage
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.


def guide(request):
    return render(request, 'guide.html')


@login_required
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
@login_required
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


# @gzip.compress
# def stream_camera(request):
#     # 웹캠 설정
#     cap = cv2.VideoCapture(0)
#     # 코덱 설정
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     # 출력 영상 설정
#     out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#     while True:
#         # 이미지 읽기
#         ret, frame = cap.read()
#         if ret:
#             # 이미지 처리 코드 작성
#             processed_frame = frame
#             # 영상 출력
#             cv2.imshow('frame', processed_frame)


# https://keep-steady.tistory.com/31

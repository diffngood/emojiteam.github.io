import cv2
import base64
import io
import logging
from django.shortcuts import render, redirect
from .models import Img, CameraImage
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


logger = logging.getLogger(__name__)


def guide(request):
    logger.info("LOGGER: Guide")
    # version = get_python_version()
    # logger.info(f"LOGGER: test {version}")
    return render(request, 'guide.html')


@login_required
def upload_img(request):
    if request.method == "POST":
        post = Img()
        post.date = timezone.now()
        post.image = request.FILES['image']
        post.save()
        logger.info("LOGGER: Upload_img successed")

        return redirect('/emo_create/detail/'+str(post.id), {'post': post})
    else:
        post = Img()
        return render(request, 'upload_img.html', {'post': post})


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

    # 이미지 처리 함수 호출
    processed_image = process_image(img.image.path)

    # 이미지 변환 및 인코딩
    _, buffer = cv2.imencode('.jpg', processed_image)
    encoded_image = base64.b64encode(buffer).decode('utf-8')

    # logger.info(f"LOGGER: Upload image url {img.image.path}")
    # logger.info(f"LOGGER: Converted image url {encoded_image}")
    return render(request, 'detail.html', {'img': img, 'processed_image': encoded_image})


def process_image(image_path):
    image = cv2.imread(image_path)

    # 이미지 처리 로직
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return processed_image

# https://keep-steady.tistory.com/31

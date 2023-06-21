import cv2
import os
from django.conf import settings
import pickle
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
        image = request.FILES.get('webcam_image')
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
    # _, buffer = cv2.imencode('.jpg', processed_image)
    # encoded_image = base64.b64encode(buffer).decode('utf-8')

    # 이미지 저장 경로
    processed_image_path = os.path.join(
        '/media/change_images/resized_image.jpg')

    logger.info(f"LOGGER: Processed_Image_Path: {processed_image_path}")

    # 이미지 저장
    cv2.imwrite(processed_image_path, processed_image)

    if request.method == 'POST':
        selected_style = request.POST.get('radio')
        # 선택한 스타일 값을 기반으로 작업 수행
        # 예를 들어, 선택한 스타일을 템플릿에 전달하여 렌더링할 수 있습니다.
        # return render(request, 'result.html', {'selected_style': selected_style})
        logger.info(f"LOGGER: selected_style: {selected_style}")
        return render(request, 'detail.html', {'img': img, 'processed_image_path': processed_image_path})

    return render(request, 'detail.html', {'img': img, 'processed_image_path': processed_image_path})


def process_image(image_path):
    try:
        # 이미지 로드
        image = cv2.imread(image_path)

        # 그레이 스케일 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # 얼굴 인식 분류기 생성
        cascade_path = os.path.join(
            settings.STATICFILES_DIRS[0], 'static/xml/haarcascade_frontalface_alt.xml')
        face_cascade = cv2.CascadeClassifier(cascade_path)
        logger.info(f"LOGGER: Cascade_Path: {cascade_path}")

        # 얼굴 인식 적용
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        logger.info(f"LOGGER: Faces: {faces}")

        # 얼굴 개수 확인
        if len(faces) == 1:
            (x, y, w, h) = faces[0]
            # 얼굴 중심으로 이미지 확대
            scale = 1.4
            cx = x + w // 2
            cy = y + h // 2
            new_w = int(w * scale)
            new_h = int(h * scale)
            x = cx - new_w // 2
            y = cy - new_h // 2
            x = max(x, 0)
            y = max(y, 0)
            new_w = min(new_w, image.shape[1] - x)
            new_h = min(new_h, image.shape[0] - y)
            cropped = image[y:y+new_h, x:x+new_w]
            resized = cv2.resize(
                cropped, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_CUBIC)
            # resized_img = cv2.resize(resized, (w, h))

            cv2.imwrite(
                "C:\\Users\\82103\\Documents\\GitHub\\emojiteam.github.io\\emojiteam.github.io\\MyEmoji\\media\\change_images\\resized_image.jpg", resized)
            return resized
    except:
        return 'error'

# 테스트
# def process_image(image_path):
#     image = cv2.imread(image_path)

#     # 이미지 처리 로직
#     processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     return processed_image


def process_style(request):
    if request.method == 'POST':
        selected_style = request.POST.get('radio')

        # 선택한 스타일에 따라 실행할 pkl 파일 경로 설정
        pkl_path = os.path.join(
            settings.BASE_DIR, 'pkl_folder', f'{selected_style}.pkl')
        logger.info(f"LOGGER: PKL 경로: {pkl_path}")

        # pkl 파일 실행
        # with open(pkl_path, 'rb') as f:
        #     model = pickle.load(f)

        # 추가적인 처리 로직 작성
        # ...

        return render(request, 'result.html', {'selected_style': selected_style, 'pkl_path': pkl_path})

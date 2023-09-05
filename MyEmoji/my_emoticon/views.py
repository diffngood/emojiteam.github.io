from django.conf import settings
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)


@login_required
def page(request):
    # 현재 로그인한 사용자의 아이디를 가져오기
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT user_id FROM styled_images WHERE user_id = %s", [username])
        user_id_exists = cursor.fetchone()
    if user_id_exists is not None:
        # SQL 쿼리 실행
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT styled_image_path0, styled_image_path1, styled_image_path2, styled_image_path3, styled_image_path4 FROM styled_images WHERE user_id = %s", [username])
            styled_image_path0 = cursor.fetchone()
            logger.info(f"LOGGER: styled_image_path_0 {styled_image_path0}")

            style_img_path_0 = styled_image_path0[0]
            style_img_path_1 = styled_image_path0[1]
            style_img_path_2 = styled_image_path0[2]
            style_img_path_3 = styled_image_path0[3]
            style_img_path_4 = styled_image_path0[4]

        logger.info(f"LOGGER: styled_image_path_0 {style_img_path_0}")
        logger.info(f"LOGGER: styled_image_path_1 {style_img_path_1}")
        logger.info(f"LOGGER: styled_image_path_2 {style_img_path_2}")
        logger.info(f"LOGGER: styled_image_path_3 {style_img_path_3}")
        logger.info(f"LOGGER: styled_image_path_4 {style_img_path_4}")
        
        return render(request, 'page.html', {'style_img_path_0': style_img_path_0, 'style_img_path_1': style_img_path_1, 'style_img_path_2': style_img_path_2, 'style_img_path_3': style_img_path_3, 'style_img_path_4': style_img_path_4})
    else:
        return render(request, 'page.html')

# 이미지 다운로드
def download_image_0(request):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path0 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path0 = cursor.fetchone()

        style_img_path_0 = styled_image_path0[0].lstrip('\\')
    processed_image_path = os.path.join(
        settings.BASE_DIR, style_img_path_0)
    with open(processed_image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename="{username}_create_img.jpg"'
        return response
    
def download_image_1(request):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path1 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path1 = cursor.fetchone()

        style_img_path_1 = styled_image_path1[0].lstrip('\\')
    processed_image_path = os.path.join(
        settings.BASE_DIR, style_img_path_1)
    with open(processed_image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename="{username}_create_img.jpg"'
        return response
    
def download_image_2(request):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path2 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path2 = cursor.fetchone()

        style_img_path_2 = styled_image_path2[0].lstrip('\\')
    processed_image_path = os.path.join(
        settings.BASE_DIR, style_img_path_2)
    with open(processed_image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename="{username}_create_img.jpg"'
        return response
    
def download_image_3(request):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path3 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path3 = cursor.fetchone()

        style_img_path_3 = styled_image_path3[0].lstrip('\\')
    processed_image_path = os.path.join(
        settings.BASE_DIR, style_img_path_3)
    with open(processed_image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename="{username}_create_img.jpg"'
        return response
    
def download_image_4(request):
    username = request.user.username
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path4 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path4 = cursor.fetchone()
        # logger.info(f"LOGGER: styled_image_path_4 {styled_image_path4}")

        style_img_path_4 = styled_image_path4[0].lstrip('\\')
    processed_image_path = os.path.join(
        settings.BASE_DIR, style_img_path_4)
    with open(processed_image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'attachment; filename="{username}_create_img.jpg"'
        return response
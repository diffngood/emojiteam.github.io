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

    # SQL 쿼리 실행
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT styled_image_path0 FROM styled_images WHERE user_id = %s", [username])
        styled_image_path0 = cursor.fetchone()

        style_img_path_0 = styled_image_path0[0]

    logger.info(f"LOGGER: styled_image_path {style_img_path_0}")
    return render(request, 'page.html', {'style_img_path_0': style_img_path_0})

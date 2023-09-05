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

# def myemo_download_image(request):
#     processed_image_path = os.path.join(
#         settings.BASE_DIR, 'static/proj.png')
#     with open(processed_image_path, 'rb') as f:
#         response = HttpResponse(f.read(), content_type="image/jpeg")
#         response['Content-Disposition'] = 'attachment; filename="processed_image.jpg"'
#         return response
from django.db import models
from PIL import Image
import os

# Create your models here.


class Img(models.Model):
    # 생략
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return str(self.id)


class CameraImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="webcam", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # 이미지를 PNG 형식으로 저장
        if self.image:
            img = Image.open(self.image.path)
            img = img.convert("RGB")

            # 이미지 저장 경로 설정
            image_path = os.path.join(
                settings.MEDIA_ROOT, 'webcam', f'{self.id}.png')

            # 이미지를 PNG 형식으로 저장
            img.save(image_path, format='PNG')

            # 저장된 이미지 경로를 self.image에 업데이트
            self.image = os.path.relpath(image_path, settings.MEDIA_ROOT)

            # 모델 저장
            self.save(update_fields=['image'])

from django.db import models

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

from django.db import models

# Create your models here.


class Img(models.Model):
    # 생략
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return str(self.title)

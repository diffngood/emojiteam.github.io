from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="images", blank=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    hit = models.PositiveIntegerField(default=0)


    @property
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()
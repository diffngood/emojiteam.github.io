from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["-pk"]
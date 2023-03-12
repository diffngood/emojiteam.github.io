from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(null=False, max_length=20)
    email = models.CharField(null=False, max_length=30)
    password = models.CharField(null=False, max_length=20)

    class Meta:
        managed = False
        db_table = 'user'

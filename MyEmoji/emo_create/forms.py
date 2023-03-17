from django.forms import ModelForm
from .models import *


class ImgForm(ModelForm):
    class Meta:
        model = Img
        fields = ('image',)

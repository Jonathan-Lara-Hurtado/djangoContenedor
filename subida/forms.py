from django import forms
from django.forms import ModelForm
from .models import Producto


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    archivo = forms.FileField()


class FormSubida(ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','descripcion','imagen','descarga']
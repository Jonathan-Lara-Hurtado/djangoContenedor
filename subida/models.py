from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
# Create your models here.
import os
from uuid import uuid4
from pagina.settings import DESCARGA_ROOT
from django.core.files.storage import FileSystemStorage
from stdimage import StdImageField, JPEGField


fs = FileSystemStorage(location=DESCARGA_ROOT)

def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(DESCARGA_ROOT, filename)

def upload_to(instance, filename):
    return 'contenido/user_{0}/{1}'.format(instance.titulo, filename)


#https://docs.djangoproject.com/en/2.2/topics/files/#the-file-object
class Producto(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    imagen = models.FileField(upload_to="almacenamiento/contenido/")
    imagenRedimencionada = StdImageField(upload_to='comprimido',
                                         variations = {'thumbnail': {'width': 224, 'height': 224,"crop": True}},
                                         delete_orphans=True,
                                         default=None)
    descarga = models.FileField(upload_to=upload_to,storage=fs)




class ProductosUser(models.Model):
    perfil = models.FileField(upload_to=upload_to)
    nonbre = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

@receiver(models.signals.post_delete, sender=ProductosUser)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """  path('almacenamiento/', include('almacenamiento.urls')),
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.perfil:
        if os.path.isfile(instance.perfil.path):
            os.remove(instance.perfil.path)


@receiver(models.signals.pre_save, sender=ProductosUser)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductosUser.objects.get(pk=instance.pk).file
    except ProductosUser.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
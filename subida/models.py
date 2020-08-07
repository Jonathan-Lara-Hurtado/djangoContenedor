from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
# Create your models here.
import  os

class Producto(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    imagen = models.FileField(upload_to="almacenamiento/contenido/")



def upload_to(instance, filename):
    return 'contenido/user_{0}/{1}'.format(instance.user.id, filename)



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
            os.remo  path('almacenamiento/', include('almacenamiento.urls')),ve(old_file.path)
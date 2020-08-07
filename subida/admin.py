from django.contrib import admin

# Register your models here.

from .models import ProductosUser,Producto

admin.site.register(ProductosUser)
admin.site.register(Producto)
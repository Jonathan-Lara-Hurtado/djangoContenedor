from django.shortcuts import render

from .forms import UploadFileForm, FormSubida
from .somewhere import handle_uploaded_file
from django.shortcuts import HttpResponse,Http404
from django.views.generic import RedirectView
from .models import Producto,wrapper
import os
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        print()
        if form.is_valid():
            handle_uploaded_file(request.FILES['archivo'].name,request.FILES['archivo'])
            return HttpResponse("que bien")
    elif request.method == 'GET':
        form = UploadFileForm()
        try:
            productos =  Producto.objects.all()
            print(productos)
        except:
            productos = None
    return render(request, 'subida/upload.html', {'form': form,
                                                  'productos':productos})


class VistaSubidaModelos(RedirectView):

    def get(self, request, *args, **kwargs):
        form = FormSubida()
        return render(request, 'subida/uploadmodelo.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST,request.FILES)
        form = FormSubida(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Agregado")
        else:
            return HttpResponse("error")



class VistaDescarga(RedirectView):

    def get(self, request, *args, **kwargs):
        print(kwargs)
        try:
            articulo = Producto.objects.get(pk=kwargs['ArticuloPk'])
        except:
            articulo = None

        if articulo is not None:
            path =str(articulo.descarga.storage.location)+"/"+str(articulo.descarga)
            if os.path.exists(path):
                file = open(path,'rb')
                response = HttpResponse(file.read(), content_type='pplication/vnd.ms-excel')
                response['Content-Disposition']='inline; filename='+ os.path.basename(path)
                return response
            raise Http404("errro")
        else:
            raise Http404("error")

    def post(self, request, *args, **kwargs):
        pass

class VistaError(RedirectView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("errooorrrrr")
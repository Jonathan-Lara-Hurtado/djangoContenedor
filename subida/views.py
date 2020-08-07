from django.shortcuts import render

from .forms import UploadFileForm, FormSubida
from .somewhere import handle_uploaded_file
from django.shortcuts import HttpResponse
from django.views.generic import RedirectView


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        print()
        if form.is_valid():
            handle_uploaded_file(request.FILES['archivo'].name,request.FILES['archivo'])
            return HttpResponse("que bien")
    else:
        form = UploadFileForm()
    return render(request, 'subida/upload.html', {'form': form})


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



class VistaModelosUser(RedirectView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
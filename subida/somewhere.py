def handle_uploaded_file(n,f):
    with open('almacenamiento/subidas/'+n, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
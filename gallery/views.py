from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse('<h1> James Webb </h1>')
    return render(request, 'gallery/index.html')

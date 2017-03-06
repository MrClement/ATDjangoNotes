from django.shortcuts import render
from django.http import HttpResponse

from .models import Dinosaur

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to webr!</h1>")


def rent(request):
    dynos = Dinosaur.objects.all()
    context = {"title": "Saurs", "dinosaurs": dynos}
    if(request.method == "POST"):
        context['error'] = "Submitted"
    return render(request, 'webr/rent.html', context)

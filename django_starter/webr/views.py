from django.shortcuts import render
from django.http import HttpResponse

from .models import Dinosaur, Rental

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to webr!</h1>")


def rent(request):
    dynos = Dinosaur.objects.all()
    context = {"title": "Saurs", "dinosaurs": dynos}
    if(request.method == "POST"):
        context['error'] = "Submitted"
    return render(request, 'webr/rent.html', context)

def rentable(request):
    date = request.GET.get('date')
    if(date):
        rented_dinos = Rental.objects.filter(rental_date=date)
        dinos = Dinosaur.objects.all()
        avail_dinos = []
        for d in dinos:
            found = False
            for r in rented_dinos:
                if(r.rented_dino.id == d.id):
                    found = True
                    break
            if not found:
                avail_dinos.append(d)
        html_to_return = ""
        for a in avail_dinos:
            html_to_return += "<option value=" + str(a.id) + ">" + a.__str__() + "</option>"
        return HttpResponse(html_to_return)
    else:
        return HttpResponse("")

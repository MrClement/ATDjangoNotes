from django.contrib import admin

# Register your models here.

from .models import Dinosaur, Rental

admin.site.register(Dinosaur)
admin.site.register(Rental)

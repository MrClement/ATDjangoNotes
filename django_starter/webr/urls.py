from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rent$', views.rent, name='rent'),
    url(r'^rentable$', views.rentable, name='rentable'),
]

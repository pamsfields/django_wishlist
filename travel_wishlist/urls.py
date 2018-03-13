from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.places_visted, name='places_visted'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
]

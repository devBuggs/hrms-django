from django.urls import path, re_path

from . import views

app_name = 'webapp'

urlpatterns = [
    # TODO: webapp urls
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
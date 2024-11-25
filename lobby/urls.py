from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.lobby, name='lobby'),
]
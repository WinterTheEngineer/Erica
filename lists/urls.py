from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.lists, name='lists'),
    path('new_list', views.new_list, name='new_list'),
]
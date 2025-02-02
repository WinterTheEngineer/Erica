from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.lists, name='lists'),
    path('new_list', views.new_list, name='new_list'),
    path('new_list_item', views.new_list_item, name='new_list_item'),
]
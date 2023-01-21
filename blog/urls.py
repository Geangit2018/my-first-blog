from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, nome = 'post_list',)
]

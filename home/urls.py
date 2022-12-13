from django.urls import re_path as url
from django.urls import path
from home import views

urlpatterns = [path('', views.home), ]

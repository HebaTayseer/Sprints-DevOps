from . import views
from .views import CoursesList
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from django.shortcuts import HttpResponse
from . import views

urlpatterns = [
    path('Welcome/', views.Welcome, name='Welcome'),
    path('list/', views.list_view, name='list'),
    path('Courses', CoursesList.as_view()),
    path('home/',views.home_view,name='home'),
    path('', views.home, name ='index'),
]

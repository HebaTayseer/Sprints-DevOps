from django.urls import path
from . import views
from .views import CoursesList

urlpatterns = [
    path('Welcome/', views.Welcome, name='Welcome'),
    path('list/', views.list_view, name='list'),
    path('Courses', CoursesList.as_view()),
]

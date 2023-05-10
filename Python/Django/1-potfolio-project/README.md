Make project called portofolio and show your cv in html page using Django . /n

1) Installing python 

2) Install a package manager like PIP 

3) Create virtual environment : python3 -m venv env_name 

4) Activate the environment : source env_name/bin/activate 

5) Install Django : python -m pip install Django 
   Check the dkango version : django-admin --version 

6) Create django project : enter to env_name folder and run this command (django-admin startproject portfolio_project) 

7) Run the django project by entering the portfolio_project folder then entering : python3 mangr.py runserver 

8) Create app in django project : python3 manage.py startapp mycv 

9)-Create a templates folder inside the cv folder, and create a HTML file named mycv.html 

10)-Modify the view as following : 
portfolio_project/students/views.py: 
from django.http import HttpResponse 
from django.template import loader 

def Welcome(request): 
template = loader.get_template('mycv.html') 
return HttpResponse(template.render()) 

11) Create file that named urls.py in app folder , and write in it as following : 
portfolio_project/students/urls.py: 
from django.urls import path 
from . import views 

urlpatterns = [ 
path('Welcome/', views.Welcome, name='Welcome’),
] 

12) Go to urls file in the project and write these : 
portfolio_project/portfolio_project/urls.py: 
from django.contrib import admin 
from django.urls import include, path 

urlpatterns = [
path('', include(‘mycv.urls')),
path('admin/', admin.site.urls),
]

13) Edit settings of the project as following :
portfolio_project/portfolio_project/settings.py:
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'mycv'
]
 

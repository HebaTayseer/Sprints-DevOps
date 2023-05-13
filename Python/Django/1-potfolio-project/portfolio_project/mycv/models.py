from django.db import models


# Create your models here.

class Students(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    birth_date = models.DateField()


class Courses(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)

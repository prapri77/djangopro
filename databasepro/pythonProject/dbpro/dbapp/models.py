from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length= 50)

class Meta:
    db_table = "employee"

class Student(models.Model):
    sid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length= 50)

class Meta:
    db_table = "student"


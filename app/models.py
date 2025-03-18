"""
Definition of models.
"""
from django.utils import timezone
from django.db import models

# Create your models here.

class Area(models.Model):
	Name = models.CharField(max_length=10,default=None,primary_key=True)
	Payment = models.CharField(max_length=20,default=None)
	Start_Time = models.CharField(max_length=20,default=None)
	End_Time = models.CharField(max_length=20,default=None)
	Order = models.BooleanField(default=False)


class User(models.Model):
	Email = models.CharField(max_length=20,default=None)
	Password = models.CharField(max_length=25,default=None)
	Money = models.IntegerField(default=0)
	NickName = models.CharField(max_length=20,default=None)
	Phone = models.CharField(max_length=20,default=None,null=True)

class Order(models.Model):
	Order_Area = models.CharField(max_length=20,default=None)
	Order_number = models.CharField(max_length=100,default=None,primary_key=True)
	Start_Time = models.CharField(max_length=20,default=None)
	End_Time = models.CharField(max_length=20,default=None)
	Email = models.CharField(max_length=20,default=None)
	Payment = models.CharField(max_length=20,default=None)

class Feedback(models.Model):
	text = models.CharField(max_length=150,default=None)
	time = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=20,default=None)
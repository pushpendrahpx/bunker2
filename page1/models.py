from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='info', null=True)
    name = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=500, unique=True)
        

    def __str__(self):
        return self.link


    def __str__(self):
        return self.name


class Bunk1(models.Model):
    class_attend = models.CharField(max_length=2)
    total_attend = models.CharField(max_length=2)
    subject = models.CharField(max_length=20, unique = True)


    def __str__(self):
        return self.class_attend
    

    def __str__(self):
        return self.total_attend

    
    def __str__(self):
        return self.subject

        
class ToDo(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDo, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text
    

class MlInfo(models.Model):
    m = models.CharField(max_length=5)
    c = models.CharField(max_length=5)
    points = models.CharField(max_length=3)

    def __str__(self):
        return self.m
    
    def __str__(self):
        return self.c
    
    def __str__(self):
        return self.points


class PtModel1(models.Model):
    item_link = models.CharField(max_length=500)
    item = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    base_price = models.CharField(max_length=100)

    def __str__(self):
        return self.base_price


    def __str__(self):
        return self.email


    def __str__(self):
        return self.item_link


    def __str__(self):
        return self.item
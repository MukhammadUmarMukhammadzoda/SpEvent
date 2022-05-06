from distutils.command.upload import upload
from pyexpat import model
from turtle import mode
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    Types = [
        ('Individual', 'Individual'),
        ('Team', 'Team')
    ]
    
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=75, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to = 'images')
    type = models.CharField(max_length=30, choices=Types, default='Team')
    date = models.DateTimeField()


    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



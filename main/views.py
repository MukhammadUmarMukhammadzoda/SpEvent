from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    event = Event.objects.all()
    context = {
        'events' : event
    }
    return render(request, 'index.html', context)
    
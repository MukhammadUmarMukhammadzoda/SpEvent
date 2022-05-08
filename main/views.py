# Importing essentialy packages
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from django.contrib import messages

#Writing Code and LOGIC
#Index PAGE
def index(request):
    event = Event.objects.all()
    context = {
        'events' : event
    }
    return render(request, 'index.html', context)
    


#Detail Page For EVENT
def detail(request, id):
    event = Event.objects.get(id = id)

    context = {
        'events' : event
    }
    return render(request, 'detail.html', context)


#Registration Page for EVENTS
def register(request, id):
    event = Event.objects.get(id = id)

    if request.method == 'POST':
        name = request.POST['name']
        tel = request.POST['phone']
        email = request.POST['email']
        faculty = request.POST['fav_language']
        a = Faculty.objects.get(id = faculty)

        data = Registration(name = name, phone = tel, email = email, faculty = a, event = event)
        data.save()
        send_mail(
            'From SpEvent Sport Activities Web site to ' + name, 
            'Hello ' + name + '. \nWe are from SpEvent. You have registred for  ' + event.name +
            ' We will wait You on ' + f'{event.date}',
            'umarbackenddeveloper@gmail.com',
            [email]
        )
        messages.success(request, f"{name} we have registred You and sent messages to Your email addres")        
        return redirect('/')

    return render(request, 'register.html', {'event' : event})


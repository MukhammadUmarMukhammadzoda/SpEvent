from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vieww/<int:id>', views.detail, name='vieww'),
    path('register/<int:id>', views.register, name='register')
    
    
    
    ]
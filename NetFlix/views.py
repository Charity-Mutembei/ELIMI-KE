from urllib import response
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def welcome(request):
    return render ( request, 'index.html')
def subjects(request):
    return render (request, 'subjects.html') 

def topics(request):
    return render (request, 'topics.html')
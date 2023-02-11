from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())

def check_kwargs(request, **kwrgs):
    return HttpResponse(f"kwargs:<br>{kwrgs}")

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.


class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Hello worldы!')


def check_kwargs(request, **kwrgs):
    return HttpResponse(f"kwargs:<br>{kwrgs}")

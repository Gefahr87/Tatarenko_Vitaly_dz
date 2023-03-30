from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.


class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Hello worldы!')


def check_kwargs(request, **kwrgs):
    return HttpResponse(f"kwargs:<br>{kwrgs}")

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'

class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Громкий новостной заголовок"
        context[
            "news_preview"
        ] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        return context

class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'

class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'

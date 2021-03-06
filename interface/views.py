from . import plot
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def error_404_view(request, exception=None):
   return render(request,'interface/error.html')

def index(request):
    template = loader.get_template('interface/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('interface/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aboutUs(request):
    template = loader.get_template('interface/aboutUs.html')
    context = {}
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template('interface/help.html')
    context = {}
    return HttpResponse(template.render(context, request))

def EEE(request):
    template = loader.get_template('interface/EEE.html')
    context = {}
    return HttpResponse(template.render(context, request))

def apiplot(request):
    return HttpResponse(plot.Layout(500,500))

def tutorialrooms(request):
    template = loader.get_template('interface/tutorialrooms.html')
    context = {}
    return HttpResponse(template.render(context, request))

def trplus(request):
    template = loader.get_template('interface/trplus.html')
    context = {}
    return HttpResponse(template.render(context, request))
import datetime
from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.
def curr_dt(request):
    now=datetime.datetime.now()
    html="<html><body><h1>It is now %s</h1></body><a href=\"https://github.com/Vigneshwaran-18\">Multiplication Table</a></html>"%now
    return HttpResponse(html)

def fha(request):
    now=datetime.datetime.now() + datetime.timedelta(hours=+4)
    html="<html><body><h1>It is now %s</h1></body><a href=\"https://github.com/Vigneshwaran-18\">Multiplication Table</a></html>"%now
    return HttpResponse(html)

def fhb(request):
    now=datetime.datetime.now() + datetime.timedelta(hours=-4)
    html="<html><body><h1>It is now %s</h1></body><a href=\"https://github.com/Vigneshwaran-18\">Multiplication Table</a></html>"%now
    return HttpResponse(html)

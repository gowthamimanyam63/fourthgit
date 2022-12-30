from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gowthami(request):
    return HttpResponse('<h2><i>This view belongs to gowthami of app1')

def sahi(request):
    return HttpResponse('<h1><B>she is lazy to be lazy</B></h1>')
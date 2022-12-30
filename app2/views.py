from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def ratish(request):
    return HttpResponse('<h1><marquee>This boy looks like innocent but not</marquee></h1>')

def mohana(request):
    return HttpResponse('<b><i>The one crazy girl</i></b>')


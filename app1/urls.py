from django.urls import path
from app1.views import *
app1_name='something1'

urlpatterns=[
    path('gowthami/',gowthami,name='gowthami'),
    path('sahi/',sahi,name='sahi'),
]
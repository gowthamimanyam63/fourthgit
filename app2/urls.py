from django.urls import path
from app2.views import *
app2_name="something2"

urlpatterns=[
    path('ratish/',ratish,name='ratish'),
    path('mohana/',mohana,name='mohana'),
]
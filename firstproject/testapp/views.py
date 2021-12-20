from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(x ):
    s="<h1>Hello Surya....Congratulations on your first djangoproject</h1>"
    return HttpResponse(s)

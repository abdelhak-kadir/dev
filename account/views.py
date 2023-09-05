from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,"account/base.html")

def request(request):
    return render(request,"account/request.html")

def europ(request):
    return render(request,"account/europ.html")

def signup(request):
    return render(request,"account/signup.html")

def liste(request):
    liste = signup.objects.all()
    return render(request,"account/liste.html",{'transporteur':liste})

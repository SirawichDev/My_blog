from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def direct_home(request):
    return HttpRequest("<h1>Home</h1>")
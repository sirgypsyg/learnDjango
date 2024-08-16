from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<hi>Blog Front Page</h1>')

# Create your views here.

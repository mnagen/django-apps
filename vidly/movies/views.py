from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#index files are in views, called by urls
def index(request):
    return HttpResponse("Hello world")

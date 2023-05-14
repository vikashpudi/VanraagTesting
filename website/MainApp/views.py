from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(route):
    return HttpResponse("Welcome to Vanraag")
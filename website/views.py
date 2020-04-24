from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def welcome(request):
    return HttpResponse('welcome to meeting planner')

def date(request):
    return HttpResponse(f'This page was served at {datetime.now()}')

def about(request):
    return HttpResponse('Hello this is Phone Thiri, rocking with Django!')
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


# Create your views here.
def welcome(request):
    num_meetings = Meeting.objects.count()
    meetings = Meeting.objects.all()
    return render(request,'website/welcome.html',{'num_meetings':num_meetings, 'meetings':meetings})

def date(request):
    return HttpResponse(f'This page was served at {datetime.now()}')

def about(request):
    return HttpResponse('Hello this is Phone Thiri, rocking with Django!')
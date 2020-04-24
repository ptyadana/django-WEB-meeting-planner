from django.shortcuts import render,get_object_or_404
from meetings.models import Meeting, Room

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html',{'meeting':meeting})

def rooms_list(request):
    num_rooms = Room.objects.count()
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms_list.html', {'num_rooms':num_rooms,'rooms':rooms})
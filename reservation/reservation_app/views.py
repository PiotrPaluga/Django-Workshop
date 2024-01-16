from django.shortcuts import render, redirect
from django.views import View
from .models import ConferenceRoom
from .forms import EditRoomForm


def add_new_room(request):
    if request.method == 'POST':
        form = EditRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            if ConferenceRoom.objects.filter(name=name).first():
                return render(request, "add-room.html", {"error": "Conference room with this name already exist",
                                                         'form': form})
            else:
                ConferenceRoom.objects.create(name=name, capacity=capacity, projector=projector)
                return redirect("room-list")
    else:
        form = EditRoomForm()
        return render(request, "add-room.html", {'form': form})


class RoomsList(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        return render(request, "rooms-list.html", {'rooms': rooms})

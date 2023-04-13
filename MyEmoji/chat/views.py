from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from chat.models import Room
from chat.forms import RoomForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# def chat(request):
#     return render(request, 'chat.html')


# def room(request, room_name):
#     return render(request, 'room.html', {
#         'room_name': room_name
#     })

def index(request: HttpRequest) -> HttpResponse:

    room_qs = Room.objects.all()
    return render(request, 'chat/index.html', {
        "room_list": room_qs,
    })
# if request.user.is_authenticated:
# else:
#     return render(request, 'login.html')


@login_required
def room_chat(requset: HttpRequest, room_pk: int) -> HttpResponse:
    room = get_object_or_404(Room, pk=room_pk)
    return render(requset, 'chat/room_chat.html', {
        "room_name": room,
    })


@login_required
def room_new(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room: Room = form.save()
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm()

    return render(request, 'chat/room_form.html', {
        "form": form,
    })

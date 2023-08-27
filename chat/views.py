from django.shortcuts import render
from . import sound
import json


def index(request):
    return render(request, 'index.html', {})


def trigger(request):
    return render(request, 'trigger.html', {})

from django.http import JsonResponse

def trigger_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duration = data.get('duration', 0)
        print(duration)
        if duration < 0.2:
            duration = 0.2

        # Perform your desired action here using the duration
        sound.play_sound(440, duration)

        message = f"Event triggered on the server! Duration: {duration} seconds"
        return JsonResponse({"message": message})
    
    return JsonResponse({"message": "Invalid request method"}, status=400)

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

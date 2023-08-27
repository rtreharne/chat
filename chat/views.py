from django.shortcuts import render
from . import sound
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html', {})


def trigger(request):
    return render(request, 'trigger.html', {})

from django.http import JsonResponse

@csrf_exempt
def trigger_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duration = data.get('duration', 0)
        print(duration)
        if duration < 0.2:
            duration = 0.2
        else:
            duration = 0.5

        # Perform your desired action here using the duration
        sound.play_sound(900, duration)

        message = f"Event triggered on the server! Duration: {duration} seconds"
        return JsonResponse({"message": message})
    
    return JsonResponse({"message": "Invalid request method"}, status=400)

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

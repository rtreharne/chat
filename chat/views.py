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
def message_event(request):
    print("Hello!")
    if request.method == "POST":

        message = json.loads(request.body).get("message", "").lower()

        first_word = message.split()[0].lower()
        if first_word in ["speak", "s", "say"]:
            message = message.replace(first_word, "", 1).strip()
            sound.text_to_speech(message)
        elif first_word in ["taunt", "pedro"]:
            sound.play_wav_file()
        elif first_word == ["morse", "m", "beep"] :
            message = message.replace(first_word, "", 1).strip()
            # if first word is number, use that as duration
            if message[0].isdigit():
                duration_factor = int(message[0])
                message = message[1:].strip()
            else:
                duration_factor = 1
            morse_output = sound.string_to_morse(message)
            sound.morse_to_sound("--", frequency=440, duration=1)
            sound.morse_to_sound(morse_output, duration=0.2/duration_factor)
            sound.morse_to_sound("..", frequency=440, duration=1)
        return JsonResponse({"message": "All Good!"}, status=200)
    return JsonResponse({"message": "Invalid request method"}, status=400)

@csrf_exempt
def trigger_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duration = data.get('duration', 0)
        print(duration)
        if duration < 0.2:
            duration = 0.2
        else:
            duration = 0.6

        # Perform your desired action here using the duration
        sound.play_sound(900, duration)

        message = f"Event triggered on the server! Duration: {duration} seconds"
        return JsonResponse({"message": message})
    
    return JsonResponse({"message": "Invalid request method"}, status=400)

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

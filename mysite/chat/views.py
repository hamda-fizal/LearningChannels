# chat/views.py
import requests
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    headers = {"authorization": ""}  # provide Assembly AI API key here.
    data = {"expires_in": 3600}
    token = ""
    try:
        response = requests.post(
            'https://api.assemblyai.com/v2/realtime/token', json=data, headers=headers)
        response_json = response.json()
        token = response_json['token']

    except Exception as e:
        print(e)

    return render(request, "chat/room.html", {"room_name": room_name, "token": token})

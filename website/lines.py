import requests

from website.models import Line


def send(data):
    line_data =  Line.objects.first()

    line_id = line_data.line_id

    token = line_data.token
    
    line_push_url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        "Content-Type":"application/json",
        "Authorization": "Bearer {" + token + "}"
    }

    text = "From: " + data['name'] + "\\n------------\\n" + data['title']

    data = '{"to": "' + line_id + '","messages":[{"type":"text", "text":"' + text + '"}]}'

    requests.post(line_push_url, headers=headers,  data = data)

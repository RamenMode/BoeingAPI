import requests
import json 

"""example call of api with GET format"""
res = requests.get('http://127.0.0.1:105/hello')
response = res.content.decode('utf-8')
print(response)

"""example call of api to send file to backend"""
with open('preamble.wav', 'rb') as fobj:
    requests.post('http://127.0.0.1:105/storeAudio', files={'fieldname': fobj})

"""example call of api to retrieve file from backend."""
res = requests.get('http://127.0.0.1:105/getAudio', params={'name': 'uploaded_audio.wav'})
print(res.content)

with open("audio.wav", 'wb') as file:
    file.write(res.content)
import requests
import constants
import pygame

CHUNK_SIZE = 1024
url =  "https://api.elevenlabs.io/v1/text-to-speech/g5CIjZEefAph4nQFvHAz?optimize_streaming_latency=0&output_format=mp3_44100_128"

headers = {
    'Accept' : 'audio/mpeg',
    'Content-Type' : 'application/json',
    'xi-api-key' : constants.Elevenlabs_APIKey
}

def TTV(response):
    print('Text to voice:\n')
    data = {
        "text" :  str(response),
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability" : 0,
            "similarity_boost": 1,
            "style": 0,
            "use_speaker_boost" : True
        }
    }

    responseVoice = requests.post(url, json=data, headers=headers)

    if responseVoice.status_code == 200:
        print('Status Code 200 - OK: The request was successful and the server returned the requested data.')
        with open('output.mp3', 'wb') as f:
            for chunk in responseVoice.iter_content(chunk_size = CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
    else:
        ErrorHandling(responseVoice)

    PlayAudio()

def ErrorHandling(response):
    #Error handling
    if response.status_code == 201:
        print('Status Code 201 - Created: The resource was successfully created.')
    elif response.status_code == 204:
        print('Status Code 204 - No Content: The request was successful, but there is no data to return.')
    elif response.status_code == 400:
        print('Status Code 400 - Bad Request: The server could not understand the request.')
    elif response.status_code == 401:
        print('Status Code 401 - Unauthorized: Authentication failed or not provided.')
    elif response.status_code == 403:
        print('Status Code 403 - Forbidden: The server understood the request, but it refuses to authorize it.')
    elif response.status_code == 404:
        print('Status Code 404 - Not Found: The requested resource does not exist.')
    elif response.status_code == 405:
        print('Status Code 405 - Method Not Allowed: The HTTP method is not allowed for this resource.')
    elif response.status_code == 500:
        print('Status Code 500 - Internal Server Error: An unexpected error occurred on the server.')
    elif response.status_code == 502:
        print('Status Code 502 - Bad Gateway: An intermediary server received an invalid response from an upstream server.')
    elif response.status_code == 503:
        print('Status Code 503 - Service Unavailable: The server is currently unable to handle the request.')
    elif response.status_code == 504:
        print('Status Code 504 - Gateway Timeout: An intermediary server did not receive a timely response.')
    else:
        print('Status code ' + str(response.status_code) + ' - Other error')
        print(str(response.content))

def PlayAudio():
        # Initialize the mixer module (for sound/music)
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("output.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()
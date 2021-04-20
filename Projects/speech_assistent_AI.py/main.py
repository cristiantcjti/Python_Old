
# what is your name?
# what time is it?
# search
# find location
# be gentle
# exit



"""
pip install speechrecognition
pip install pyaudio (if it does not work, isntall pipwiw and then pipwin install pyaudio)
pip install gTTS
pip install playsound
pip install PyObjC (MacOs )
"""
import speech_recognition as sr 
import webbrowser
import time
import os
import random
from time import ctime
#import playsound
#import gTTS
#from gTTS import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone(device_index=2) as source:
        if ask:
            print(ask)
        print('You can say:')
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('I am so sorry but I did not get that')
        except sr.RequestError:
            print('Sorry, but the speech service is not working')
        return voice_data

"""
def assistent_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
"""

def answer(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Helper')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you what to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open('https://mobi2buy.com/') #https://mobi2buy.com/ #https://www.agriness.com/en/
        #webbrowser.get().open('https://mobi2buy.com/')
        #webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('Where would you like the location for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'be gentle' in voice_data:
        print("Hi interviwers")
    if 'exit' in voice_data:
        exit()


time.sleep(1)
print('Hello, how can I help you?')
while True:
    voice_data = record_audio()
    answer(voice_data)    



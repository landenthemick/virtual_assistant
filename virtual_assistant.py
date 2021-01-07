import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#   ignore any warnings
warnings.filterwarnings('ignore')

#   record audio (return audio as a string)
def audiopickup():

    r = sr.Recognizer()

    #   open microphone
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    # google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError


#(to be continued) currend date: January 5th, 2021


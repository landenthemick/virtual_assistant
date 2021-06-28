# Virtual Assistant program that can assist the user with many different tasks.

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

#Import Neccesary Libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#Ignore warning messages inside of program
warnings.filterwarnings('ignore')

#Record audio, return as a string
def recordAudio():

    #record the audio
    r = sr.Recognizer() #recognizes the audio

    #activate microphone
    with sr.Microphone() as source:
        print('Speak command')
        audio = r.listen(source)

    #Utlize Google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError: #check for unknown errors
        print('Audio not recieved, UnknownError')
    except sr.RequestError as e:
        print('Google Speech Recognition error'+ e)

    return data

recordAudio()
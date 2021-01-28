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
    except sr.UnknownValueError:
        pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

def Commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return ""
    return query

def chrome(chrome_path, url):
    webbrowser.get(using = chrome_path).open(url)
    
def default(url):
    webbrowser.open(url)

if __name__ == "__main__":
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    end = ("quit", "close", "leave","bye")
    greet()
    done= False
    while not done:
        url = ""
        query = Commands().lower()
        for val in end:
            if val == query:
                speak("Have a good day.")
                done = True  

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            url = "youtube.com"

        elif 'google' in query:
            url = "google.com"

        elif 'netflix' in query:
            url = "netflix.com" 
            
        elif 'open pycharm' in query:
            try:
                codePath = "/Applications/PyCharm CE.app" 
                os.startfile(codePath)
            except:
                try:
                    jetBrainDir = "C:/Program Files/JetBrains/"
                    jetbrainApps = os.listdir(jetBrainDir)
                    for f in jetbrainApps:
                        if "PyCharm" in f:
                            pycharmDir = os.path.join(jetBrainDir, f)
                            break
                    binDir = os.path.join(pycharmDir, "bin")
                    binFiles = os.listdir(binDir)
                    pycharmExecutablePattern = (r'pycharm[0-9]{2}.exe')
                    for f in binFiles:
                        if re.match(pycharmExecutablePattern, f):
                            absolutePyCharmDir = os.path.join(binDir, f)
                            break
                    
                    os.startfile(absolutePyCharmDir)
                except:
                    print("Could not find path for PyCharm")
                    
              

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)

engine.setProperty('voice',voices[1].id)
# print(voices[0].id)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("hello sir, i am your Assistant please tell me how may i help you ")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_thresold=1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
        c="you said"+query
        #speak(c)
    except Exception as e:
        print(e)
        print("say that again please....")
        return "none"
    return query
speak('hello')
wishme()
b=True
while b:
    query=takecommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=2)
        speak('according to wikipedia ..')
        speak(results)
    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'play music' in query:
        music="G:\\song\\80s hits"
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music,songs[0]))
    elif 'exit' in query:
        b=False

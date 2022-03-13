import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

engine= pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")
    elif hour>=12 and hour<18:
        say("Good Afternoon!")
    else:
        say("Good Night")

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")        
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            print("Recognition...")
            query=r.recognize_google(audio,language='en-in')
            print(f"You said:{query}")
        except Exception as e:
            print("Say that again please...")
            print(e)
            return "None"
        return query

if __name__=="__main__":
    wish()
    say("Hi I am Desktop assistant ,how can I help you")
    while True:
        query = listen().lower()

        if 'open google' in query:
            say("opening google")
            webbrowser.open("google.com")
            break
        
        elif 'open youtube' in query:
            say("opening youtube")
            webbrowser.open("youtube.com")
            break

        elif 'wikipedia' in query:
            try:
                say('Searching Wikipedia...')
                query=query.replace("wikipedia","")
                results= wikipedia.summary(query,sentences=2)
                say("According to Wikipesia")
                print(results)
                say(results) 
            except Exception as e:
                print(e)
        elif 'what is' in query:
            try:
                say('Searching Wikipedia...')
                query=query.replace("wikipedia","")
                results= wikipedia.summary(query,sentences=2)
                say("According to Wikipesia")
                print(results)
                say(results) 
            except Exception as e:
                print(e)
        elif 'who is' in query:
            try:
                say('Searching Wikipedia...')
                query=query.replace("wikipedia","")
                results= wikipedia.summary(query,sentences=2)
                say("According to Wikipesia")
                print(results)
                say(results) 
            except Exception as e:
                print(e)

        elif 'play music' in query:
            listmusic='C:\\Users\\singh\\Music'
            songs=os.listdir(listmusic)
            os.startfile(os.path.join(listmusic,songs[0]))
            break

        elif 'open code' in query:
            codepath="C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            say("opening visual studio code")
            break

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir time is{time}")
            print(time)

        elif 'who are you' in query:
            say("I am Desktop assistant")
       
        elif 'ok bye' in query:
            say("ok")
            break
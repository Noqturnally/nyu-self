import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import comtypes


print('Loading NYU - The one and only')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    strTime=datetime.datetime.now().strftime("%H:%M")
    if hour>=0 and hour<12:
        speak("Hello,Good Morning It's currently" + strTime )
        print("Hello,Good Morning It's currently" + strTime)
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon It's currently" + strTime)
        print("Hello,Good Afternoon It's currently" + strTime)
    else:
        speak("Hello,Good Evening It's currently" + strTime)
        print("Hello,Good Evening It's currently" + strTime)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening with my sharp ears..")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"Your statement was: {statement}\n")

        except Exception as e:
            speak("AHHH This mic sorry say again")
            return "None"
        return statement

speak("Loading Nyu the kawaii assistant")
wishMe()


if __name__=='__main__':


    while True:
        speak("Now what should I do?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('I gotta go sleep bye might meet you again')
            print('I gotta go sleep bye might meet you again -_-')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Gotcha buddy youtube here")
            print("Gotcha buddy! YouTube here")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Chrome joined the battle")
            print("Chrome joins the battle..... <o>")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("WOOO your account is mine")
            print("WOOO! Your account is mine now.")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Where do you live")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("Actually where the heck do you live")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Nyu a virtual-assistant that can talk , search open chrome and do much more...')
            print("I am Nyu a virtual-assistant that can talk , search open chrome and do much more...")
            speak('I like chocolate ice-cream and linux-systems')
            print("I like chocolate ice-cream and linux-systems")


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I am built by Abhinav or Nocturnal")
            print("I am built by Abhinav or Nocturnal")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Just get better")
            print("xD (just kidding)")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Seriously, you could have bought one but enjoy')
            print("Seriously, you could have bought one but enjoy <3")
            time.sleep(6)


        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)


time.sleep(3)













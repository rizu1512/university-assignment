
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import cv2
from PyDictionary import PyDictionary
import numpy as np

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
cap =cv2.VideoCapture(0)



def talk(text):
    engine.say(text)
    engine.runAndWait()
   
#def game():
 #   engine = pyttsx3.init()
  #  volume = engine.getProperty('volume')
   ##engine.say('The quick brown fox jumped over the lazy dog.')
    #engine.runAndWait()

def ter(sef,cap):
            cap.release()
            cv2.destroyAllWindows()
            quit()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('current time is ' + time)
        talk('Current time is ' + time)
        
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'send message' in command:
        pywhatkit.sendwhatmsg("+923484608969","how are you",10,)
    elif 'open google' in command:
        webbrowser.open('https://www.google.com/')
        talk('opening Google')
    elif 'open facebook' in command:
        webbrowser.open('https://www.facebook.com/')
        talk('opening Facebook')
    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com/')
        talk('opening Youtube')
    elif 'open twitter' in command:
        webbrowser.open('https://twitter.com/')
    elif 'open gmail' in command:
        print('Gmail is opening')
        talk('Gmail is opening')
        webbrowser.open('https://gmail.com/')
    elif 'text convert' in command:
        talk("text convert in to handwriting form")
        pywhatkit.text_to_handwriting('hi my name is',save_to="han.png")
        img=cv2.imread("han.png")
        cv2.imshow("text to handwriting",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif 'open microsoft edge' in command:
        codepath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        os.startfile(codepath)
        talk('opening Microsoft Edge')
   
    elif 'open chrome' in command:
        codepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codepath)
        talk('open your Google Chrome')
    elif 'open ms word' in command:
        codepath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
        os.startfile(codepath)
        talk('open your Ms Word')
    elif 'open excel' in command:
        codepath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
        os.startfile(codepath)
        talk('open your Excel')
    elif 'open powerpoint' in command:
        codepath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
        os.startfile(codepath)
        print('open your power point')
        talk('open your power point')
    elif 'open camera' in command:
        print('Camera is opening')
        talk('Camera is opening')
        while True:
            ret,frame =cap.read()
            cv2.imshow('frame',frame)
            k=cv2.waitKey(10) & 0xff
            if k==27: 
                break
        cap.release()
        cv2.destroyAllWindows()
        quit()
    elif 'turn off camera' in command:
        ter()
    else:
        talk('Please say the command again.')



while True:
    run_alexa()

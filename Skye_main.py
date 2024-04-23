from ast import keyword
import datetime
import os
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import pyautogui
import random
import webbrowser





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break

                elif "hello sky" in query:
                    print("Hello sir, how are you ?")
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    print("that's great, sir")
                    speak("that's great, sir")
                elif "how are you" in query:
                    print("Perfect, sir")
                    speak("Perfect, sir")
                elif "nice" in query:
                    print("you are welcome, sir")
                    speak("you are welcome, sir")

                
                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)



                elif "stop" in query:
                    pyautogui.press("k")
                    print("video stoped")
                    speak("video stoped")
                elif "play" in query:
                    pyautogui.press("k")
                    print("video played")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    print("video muted")
                    speak("video muted")
                elif "umute" in query:
                    pyautogui.press("m")
                    print("video unmuted")
                    speak("video unmuted")
                elif "full screen" in query:
                    pyautogui.press("f")
                    print("done sir")
                    speak("done sir")
                elif "small screen" in query:
                    pyautogui.press("f")
                    print("done sir")
                    speak("done sir")

                elif "volume up" in query:
                    from keyboard import volumeup
                    print("Turning volume up,sir")
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    print("Turning volume down, sir")
                    speak("Turning volume down, sir")
                    volumedown()
                


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query) 
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                # elif "temperature" in query:
                #     search = "temperature in delhi"
                #     url = f"https://www.google.com/search?q={search}"
                #     r  = requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parser")
                #     temp = data.find("div", class_ = "BNeawe").text
                #     speak(f"current{search} is {temp}")
                # elif "weather" in query:
                #     search = "temperature in delhi" 
                #     url = f"https://www.google.com/search?q={search}"
                #     r  = requests.get(url)
                #     data = BeautifulSoup(r.text,"html.parser")
                #     temp = data.find("div", class_ = "BNeawe").text
                #     speak(f"current{search} is {temp}")
               
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(strTime)        
                    speak(f"Sir, the time is {strTime}")

                elif "the date" in query:
                    strDate = datetime.datetime.now().strftime("%B %d,%Y")
                    print(strDate)    
                    speak(f"Sir, the date is {strDate}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Sky","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())


                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=yXdjud6zBbY")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=I_1WUDYh1NY")


                    # elif "news" in query:
                    #     from NewsRead import latestnews
                    #     latestnews()

                # elif "calculate" in query:
                #     from Calculatenumbers import WolfRamAlpha
                #     from Calculatenumbers import Calc
                #     query = query.replace("calculate","")
                #     query = query.replace("jarvis","")
                #     Calc(query)



                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                # elif "shutdown the system" in query:
                #     speak("Are You sure you want to shutdown")
                #     shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                #     if shutdown == "yes":
                #         os.system("shutdown /s /t 1")

                #     elif shutdown == "no":
                #         break     
                
                elif "open" in query:   #EASY METHOD
                                    query = query.replace("open","")
                                    query = query.replace("sky","")
                                    pyautogui.press("super")
                                    pyautogui.typewrite(query)
                                    pyautogui.sleep(2)
                                    pyautogui.press("enter") 
               
                                    
                # elif "internet speed" in query:
                #                     import speedtest
                #                     wifi  = speedtest.Speedtest()              #pip install speedtest-cli
                #                     upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                #                     download_net = wifi.download()/1048576
                #                     print("Wifi Upload Speed is", upload_net)
                #                     print("Wifi download speed is ",download_net)
                #                     speak(f"Wifi download speed is {download_net}")
                #                     speak(f"Wifi Upload speed is {upload_net}")                                               

               
               
               
                elif "have a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                                    pyautogui.press("super")
                                    pyautogui.typewrite("camera")
                                    pyautogui.press("enter")
                                    pyautogui.sleep(5)
                                    speak("SMILE")
                                    pyautogui.press("enter")
                



                elif "finally sleep" in query:
                    speak("Going to sleep,sir")

                    exit()
                    

                

                





                    
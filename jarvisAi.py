import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
#print(voices[1].id)
engin.setProperty('voice',voices[0].id)
def speak(audio):
    engin.say(audio)
    engin.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir. please tel me how may i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query
def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashutoshpatel14022000@gmail.com','your - ashutosh@2000')
    server.sendmail('ashutoshpatel14022000@gmail.com',to ,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            statTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {statTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\ashut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to ashu' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "ashutoshpatel14022000@gmail.com"
                sendEmail(to,content)
                speak("Email has send")
            except Exception as e:
                print(e)
                speak("Sorry my friend ashu bhai. I am not able to send this email")
        elif 'open opera Browser' in query:
            webbrowser.open("opera.com")

        if 'quit' in query:
            exit()




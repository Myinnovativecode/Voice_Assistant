# Voice Activated Personal Assistant
import json
import pygame
import pyttsx3
import webbrowser
import os
import smtplib
import wikipedia
import datetime
import random
import requests
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to female

pygame.mixer.init()

def sendEmail(emailAdd, content):
    with open('pass.txt', 'r') as file:
        password = file.read().strip()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('janviprajapat18022004@gmail.com', password)
    server.sendmail('janviprajapat18022004@gmail.com', emailAdd, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello, this is Myraa. How can I help you today?")

def takeCommand():
    '''
    Takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-In")
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def fetch_news():
    speak("What type of news are you interested in?")
    typeNews = takeCommand()

    if typeNews is None:
        speak("Sorry mam, I couldn't hear your query. Please try again.")
        return

    # Refine the query for specific topics related to India
    url = f"https://newsapi.org/v2/everything?q={typeNews}+India&language=en&from=2024-10-24&sortBy=publishedAt&apiKey=bea71fbef37a446b902322aad5967ab5"

    r = requests.get(url)
    news = json.loads(r.text)

    # Check if there are articles
    if news.get("status") == "ok" and len(news["articles"]) > 0:
        speak(f"Here are the top 2 news articles on {typeNews}:")
        # Loop through the first 2 articles and read out the details
        for i, article in enumerate(news["articles"][:2]):
            title = article.get("title", "No title available")
            description = article.get("description", "No description available")
            content = article.get("content", "No content available")

            # Read out the article title, description, and content
            speak(f"Headline {i + 1}: {title}")
            speak(f"Description: {description}")
            speak(f"Content: {content[:10]}...")  # Reading only the first 20 characters of the content as a sample

            print(f"Headline {i + 1}: {title}")
            print(f"Description: {description}")
            print(f"Content: {content[:10]}...")
            print("-----------------------------------------------------------------")
    else:
        speak("Sorry mam, I couldn't find any news articles related to your query.")

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia.")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Multiple results found, could you be more specific? Here are some options: {e.options}")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("Sorry mam, I couldn't access Wikipedia. Please check your internet connection.")
            except Exception as e:
                speak("Sorry mam, there was an error. Please try again.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query or 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            music_dir = "D:\\Music"
            music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
            random_song = random.choice(music_files)
            song_path = os.path.join(music_dir, random_song)
            speak(f"Now playing: {random_song}")
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
            print(strTime)

        elif 'open vs code' in query or 'open visual studio code' in query:
            codePath = "C:\\Users\\akpad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # Command for reading news
        elif 'read the newspaper' in query or 'newspaper reading' in query:
            fetch_news()

        # Handle exit commands
        elif any(word in query.lower() for word in ['good bye', 'bye', 'exit', 'close', 'stop', 'quit']):
            speak("Okay, I’ll be quiet. You can wake me up when you need help.")
            print("Okay, I’ll be quiet. You can wake me up when you need help.")
            break  # Exits the program

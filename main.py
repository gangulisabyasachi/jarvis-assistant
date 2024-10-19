import speech_recognition as sr
import webbrowser
import pyttsx3
import dataset
from dataset import webLibrary, music  # Adjust the import based on your directory structure

import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "api-key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# the below snippet is for google aunty voice. make the previous one as speak_old
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="api-key",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    c = c.lower()  # Convert command to lowercase for easier comparison

    # Open websites from webLibrary
    for site in webLibrary:
        if f"open {site}" in c:
            webbrowser.open(webLibrary[site])
            return  # Exit after opening the website

    # Play songs from music dataset
    if c.startswith("play"):
        song = " ".join(c.split(" ")[1:])  # Get the song name after "play"
        link = music.get(song)  # Use get to avoid KeyError
        if link:
            webbrowser.open(link)  # Open the song link
        else:
            print(f"Sorry, I couldn't find the song '{song}' in the music library.")
    
    # News command
    elif "khabar" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)  

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))



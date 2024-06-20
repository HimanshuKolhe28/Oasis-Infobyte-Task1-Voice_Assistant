"""
Idea: Voice Assistant
Description:
For Beginners: Create a basic voice assistant that can perform simple tasks based on voice commands. Implement features like responding to "Hello" and providing predefined responses, 
telling the time or date, and searching the web for information based on user queries.
"""


import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import time  # Import time module for sleep function

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, there is an issue with the speech service.")
            return None

def respond(command):
    """Respond to the voice command."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    else:
        speak("Sorry, I didn't understand that command.")

    # Pause briefly to allow the speech to finish before listening again
    time.sleep(1)

def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            respond(command)

main()

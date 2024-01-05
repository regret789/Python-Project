import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyjokes

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""


def speak(text):
    engine = pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)

    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

def assistant():
    speak("Hi! I'm your voice assistant. How may I help you?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello shambhu!")

        elif "what is your name" in query:
            speak("My name is Jarvis From Nepal and I am your assistant.")

        elif " How old are you" in query:
            speak("I am 15 years old and How old are you?")

        elif "what time is it" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "search on the web" in query:
            speak("Sure, what would you like me to search?")
            search_query = listen()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif "open youtube" in query:
            speak("Sure, which channel would you like me to open?")
            youtube = listen()
            webbrowser.open("https://www.youtube.com/")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "exit" in query:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    assistant()

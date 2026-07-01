# ==========================================
# Voice Assistant (Part 1)
# Windows 10 + Python 3.12
# ==========================================

import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import datetime

# -----------------------------
# Voice Engine
# -----------------------------
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

if len(voices) > 0:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

# -----------------------------
# Speech Recognizer
# -----------------------------
recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.pause_threshold = 1
recognizer.dynamic_energy_threshold = True

# -----------------------------
# Speak Function
# -----------------------------
def speak(text):
    print("Assistant :", text)
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Listen Function
# -----------------------------
def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=5
            )

        except sr.WaitTimeoutError:
            return ""

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You :", command)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection is required.")
        return ""

    except Exception as e:
        print(e)
        return ""

# -----------------------------
# Greeting
# -----------------------------
def wish():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your Voice Assistant.")
    speak("How can I help you?")

    # ==========================================
# Commands (Part 2)
# ==========================================

def execute_command(command):

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open chatgpt" in command or "open chat g p t" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "open chrome" in command:
        speak("Opening Chrome")
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif "open edge" in command:
        speak("Opening Microsoft Edge")
        subprocess.Popen("msedge")

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    elif "open paint" in command:
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")

    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")

    elif "open file explorer" in command or "open explorer" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")

    elif "open camera" in command:
        speak("Opening Camera")
        os.system("start microsoft.windows.camera:")

    elif "open settings" in command:
        speak("Opening Settings")
        os.system("start ms-settings:")

    elif "open control panel" in command:
        speak("Opening Control Panel")
        subprocess.Popen("control")

    elif "open task manager" in command:
        speak("Opening Task Manager")
        subprocess.Popen("taskmgr")

    elif "what is the time" in command or "tell me the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "what is the date" in command or "today's date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "who are you" in command:
        speak("I am your Python Voice Assistant.")

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye. Have a nice day.")
        return False

    elif command != "":
        speak("Sorry, I don't know that command yet.")

    return True
# ==========================================
# Main Program (Part 3)
# ==========================================

def main():

    wish()

    while True:

        command = listen()

        if command == "":
            continue

        # Search Google
        if command.startswith("search google for"):
            query = command.replace("search google for", "").strip()

            if query:
                speak(f"Searching Google for {query}")
                webbrowser.open(
                    "https://www.google.com/search?q=" + query.replace(" ", "+")
                )
            continue

        # Search YouTube
        if command.startswith("search youtube for"):
            query = command.replace("search youtube for", "").strip()

            if query:
                speak(f"Searching YouTube for {query}")
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" +
                    query.replace(" ", "+")
                )
            continue

        # Open VS Code
        if "open visual studio code" in command or "open vs code" in command:
            speak("Opening Visual Studio Code")

            try:
                subprocess.Popen("code")
            except:
                speak("VS Code command was not found.")
            continue

        # Open Spotify
        if "open spotify" in command:
            speak("Opening Spotify")

            try:
                os.system("start spotify:")
            except:
                speak("Spotify is not installed.")
            continue

        # Open WhatsApp
        if "open whatsapp" in command:
            speak("Opening WhatsApp")

            try:
                os.system("start whatsapp:")
            except:
                speak("WhatsApp Desktop is not installed.")
            continue

        running = execute_command(command)

        if not running:
            break


if __name__ == "__main__":
    main()
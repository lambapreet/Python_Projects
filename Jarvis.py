import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def execute_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    
    elif 'play music' in command:
        kit.playonyt("your favorite song")  # Replace with your favorite song
        speak("Playing music")
    
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    
    elif 'what is your name' in command:
        speak("I am your virtual assistant, Jarvis.")
    
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I am sorry, I cannot help with that.")

def main():
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        execute_command(command)

if __name__ == "__main__":
    main()
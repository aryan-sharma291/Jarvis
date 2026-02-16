# afplay
import pyaudio
import pyttsx3
import random
engine = pyttsx3.init()

text = input("type the text you want the computer to say: ")
if not text:
    text = "Hello World!"
engine.say(text)

number = random.randint(1, 100000000)
engine.save_to_file(f"{text}", f"{text}-{number}.wav")

engine.runAndWait()

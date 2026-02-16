# afplay
import openai
import datetime
import random
def date_format(dt_object):
    # This takes a datetime object and turns it into a filename-safe string
    return dt_object.strftime("%m-%d-%Y_%H-%M-%S")

client = openai.OpenAI(
    api_key="Your Api Key"

)
import pyaudio
import speech_recognition as sr
import pyttsx3
import importlib
user_text = ""
# obtain audio from the microphone
r = sr.Recognizer()
engine = pyttsx3.init()

while True:


    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Say something!")
        audio = r.listen(source, timeout=5, phrase_time_limit=100)



    try:
        user_text = r.recognize_google(audio)
        print("You said:" + " " + user_text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        user_text = ""
        continue


    try:
        if user_text.lower() == "stop":
            print("Stopping...")
            break
        elif user_text.lower() == "change mode":
            mode = input("what mode would you like to use?(V/T)")
            user_text = "mode changed to " + mode
            continue
        elif user_text != "":
            response_text = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                        {"role": "system", "content": "Speak like Jarvis in the Iron Man movies I am a man, my name is Aryan Sharma."},
                        {"role": "user", "content": user_text}
                ],
                max_tokens=100
            )
            final_rely = response_text.choices[0].message.content
        else:
            final_rely = "i dont know what you are doing"
    except openai.APIConnectionError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        final_rely = "Could not request results from Google Speech Recognition service; {0}".format(e)

    print("Jarvis said:" + " " + final_rely)
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()
    engine.say(final_rely)
    date = datetime.datetime.now()
    engine.save_to_file(f"{final_rely}", f"{user_text.replace(' ', '_')}_{date_format(date)}.wav")

    engine.runAndWait()
    engine.stop()
    del engine



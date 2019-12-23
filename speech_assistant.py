import speech_recognition as sr
from time import ctime
import webbrowser

# Create an object
r = sr.Recognizer()

def record_speech(question = ""):
    # Use microphone as speech source
    with sr.Microphone() as source:
        if question:
            print(question)

        speech = r.listen(source)
        speech_text = ""

        try:
            speech_text = r.recognize_google(speech)
            print("Oh My Goodness! This Is What You Have Just Asked For:\n")
        except sr.UnknownValueError:
            print("Sorry, I Could Not Understand What You Have Just Said.\n")
        except sr.RequestError:
            print("Sorry, I Could Not Connect To The Internet. Resolve The Issue And Come Back.")

        return speech_text


def respond_to_speech(speech_text):
    if "what time is it" in speech_text:
        print(ctime())
    
    if "find location" in speech_text:
        location = record_speech("What is the location?")

        url = "https://google.com/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)

        print("The location " + location + " has been found.")


print("Tell Me What You Would Like To Do And I Will Do It For You.\n")
speech_text = record_speech()

respond_to_speech(speech_text)

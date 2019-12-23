import speech_recognition as sr

# Create an object
r = sr.Recognizer()

# Use microphone as speech source
with sr.Microphone() as source:
    print("Tell me what you want and I write it for you.\n")
    speech = r.listen(source)

    try:
        speech_text = r.recognize_google(speech)
        print("This is what you have said:\n")
        print(speech_text)
    except sr.UnknownValueError:
        print("I could not understand what you said.\n")

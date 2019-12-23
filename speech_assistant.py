import speech_recognition as sr

# Create an object
r = sr.Recognizer()

# Use microphone as speech source
with sr.Microphone() as source:
    print("What's on your mind?")
    
    speech = r.listen(source)
    speech_text = r.recognize_google(speech)

    print(speech_text)


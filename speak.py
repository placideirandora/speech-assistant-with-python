import os
import random
from gtts import gTTS
import playsound

def speak(speech_text):
    tts = gTTS(speech_text, lang="en")
    
    random_number = random.randint(1, 1000)
    audio_file = "speech-" + str(random_number) + ".mp3"
    
    tts.save(audio_file)
    playsound.playsound(audio_file)
    
    print(speech_text)
    os.remove(audio_file)
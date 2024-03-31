from gtts import gTTS
import os


def speak(message):
    pass
    # Language in which you want to convert
    language = 'en'
    message = "." + message
    myobj = gTTS(text=message, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file
    myobj.save("audiofile.mp3")

    # Playing the converted file
    # linux audio
    os.system("mpg321 audiofile.mp3")
    # MacOS
    # os.system("afplay audiofile.mp3")


# speak("Hello World")
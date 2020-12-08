import speech_recognition as sr
import pyttsx3
import pywhatkit

listner = sr.Recognizer()
arya = pyttsx3.init()

def talk(text):
    arya.say(text)
    arya.runAndWait()

talk("i am bob your personal assistant how can i help you")

def talk_process():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'bob' in command:
                command = command.replace('bob','')
                print(command)


    except:
        pass

    return command

def run_bob():
    command = talk_process()

    if 'play' in command:
        song = command.replace('play','')
        talk('ok, playing')




run_bob()
import pyttsx3

voz = pyttsx3.init('sapi5')
while True:
    voz.say(str(input('MSG: ')))
    voz.runAndWait()
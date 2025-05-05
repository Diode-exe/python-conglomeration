import pyttsx3

# Initialize pyttsx3 for speaking
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Getting the text to speak
print("Welcome to the voice")
voiceToSay = input("What would you like the voice to say? ")

# Asking if the user wants to see the list of voices
listVoices = input("Would you like to see the list of voices? yes or no (case sensitive): ")

if listVoices == "yes":
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} ({voice.id})")

# Choosing the voice
voice = int(input("Type the number for the voice: "))

if 0 <= voice < len(voices):
    engine.setProperty('voice', voices[voice].id)
else:
    print("Invalid voice number.")

# Setting volume and rate
voiceVolume = input("Choose the volume, 0.1-1.0: ")
voiceRate = input("Choose the rate for the voice: ")

try:
    engine.setProperty('volume', float(voiceVolume))
    engine.setProperty('rate', int(voiceRate))
except ValueError:
    print("Invalid volume or rate. Using defaults.")
engine.setProperty('voice', voices[voice].id)

# Speaking the text
engine.say(voiceToSay)
engine.runAndWait()

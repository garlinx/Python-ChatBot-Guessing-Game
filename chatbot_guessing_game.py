import speech_recognition as sr
import pyttsx3
import random
import wikipedia

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[2].id)
    engine.say(command)
    engine.runAndWait()
  
with sr.Microphone() as source:
    
    f = open("fruits.txt", "r")
    fruits = []
    for line in f:
        fruits.append(line.strip())
    #print(fruits)    
    
    fruit = random.choice(fruits).lower()
    #print(fruit)
    num_guesses = 3
    
    # Checking background noise....
    r.adjust_for_ambient_noise(source, duration=2)
    
    SpeakText("I am thinking of a fruit.")
    SpeakText("You have three tries to guess what it is.")
    SpeakText("What is your first guess?")
    
    for i in range(num_guesses):

        # Listen for the user's input
        audio = r.listen(source)
        
        # Using google to recognize audio
        guess = r.recognize_google(audio)
        
        if guess == fruit:
            SpeakText(guess + " is correct! You win.")
            print(guess + " is correct! You win.")
            break
        elif i < num_guesses-1:
            SpeakText(guess + " is incorrect. Try again.")
            print(guess + " is incorrect. Try again.")
        else:
            SpeakText(guess + " is incorrect. Sorry, you lose. The word I was thinking of was " + fruit)
            print(guess + " is incorrect.\nSorry, you lose. The word I was thinking of was " + fruit)
            break

with sr.Microphone() as source:
    
    # Checking background noise....
    #r.adjust_for_ambient_noise(source, duration=1)
    
    SpeakText(f"Do you know what the fruit {fruit} is?")
    
    audio = r.listen(source)
    
    # Using google to recognize audio
    reply = r.recognize_google(audio)
    
    if "yes" in reply:
        SpeakText('OK, thanks for playing. Good bye!!')
    else:
        # Asking Wikipedia for a definition
        print(wikipedia.summary(f"{fruit} the fruit"))
        SpeakText(wikipedia.summary(f"{fruit} the fruit"))

        
    

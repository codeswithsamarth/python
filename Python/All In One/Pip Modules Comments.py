# Modules is A file contanies code which is written by someone else we import it use this in our programs.
import pyttsx3
engine = pyttsx3.init()
text = input("Enter Text For To Proceed:")
engine.say(text)
engine.runAndWait()

import pyjokes
jokes = pyjokes.get_joke()
print(jokes)


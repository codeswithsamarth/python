import pyttsx3
engine = pyttsx3.init()
users_inp = input("Enter Your text")
engine.say(users_inp)
engine.runAndWait()

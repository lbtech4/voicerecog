import pyaudio
import os
import speech_recognition as sr
mic = sr.Microphone()
r = sr.Recognizer()


while True:
    with mic as source:
        ad = r.listen(source)
        try:
            print("Recognizing...")
            print(r.recognize_google(ad))
            if "School" in r.recognize_google(ad):
                os.system("start https://adams12.schoology.com/course/3117478194/materials")
            if (ad == "zoom"):
                os.system("start https://adams12.schoology.com/course/3117478194/materials/link/view/3191466209")
            
            if "my files" in r.recognize_google(ad):
                    print("Getting Files")
                    os.system("echo/YourFilesAre: & echo/ & dir /b & echo/")
        except:
            print("Sorry - we could not hear what you said. Please try again")
            
            


        

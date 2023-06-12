import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

#this method is for taking the commands and recognizing the command from the speech_recognition module we wil use the recognizer method for recognizing
def takeCommand():

    r = sr.Recognizer()

    #we will use the microphone module for listening the command
    with sr.Microphone() as source:
        print('Listening')

        #seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        #if sound is recognized it is good, else we will have exception handling
        try:
            print("Recognizing")

            #only commands in english, but by changing 'en-in' you can pick other language

            Query = r.recognize_google(audio, language = 'en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again, please")
            return "None"
        
        return Query
    
def speak(audio):
    engine = pyttsx3.init()

    #getter method(gets the current value of engine property)

    voices = engine.getProperty('voices')

    #setter method .[0]=male voice and [1]= female voice in set Property
    engine.setProperty('voice', voices[0].id)

    #method for the speaking of the assistant
    engine.say(audio)

    #blocks while processing all the currently queued commands
    engine.runAndWait()

def tellDay():

    #this function is for telling the day of the week
    day = datetime.datetime.today().weekday() + 1

    #this line tells us about the number that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("the day is" + day_of_the_week)

def tellTime():

    #this method will give the time
    time = str(datetime.datetime.now())

    #the time will be displayed as per example "2020-06-05 17:50:14.582630" and then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is " + hour + "Hours and " + min + "Minutes")

def Hello():

    #this function is for when the assistant is called it will say hello and then take query
    speak("hello, I am your desktop assistant. Tell me how may I help you") 

def Take_query():

    #calling the hello function for making it more interactive
    Hello()

    #this loop is infinite as it will take our queries continously until and unless we do not say bye to exit or terminate the program
    while(True):
        
        #taking the query and making it into lower case so that most of the times query matches and we get the perfect output

        query = takeCommand().lower()
        if "open wikipedia" in query:
            speak("Opening Wikipedia")

            #in the open method we just give the link of the website and it automatically open it in your default browser
            webbrowser.open("www.wikipedia.com")
            continue
            
        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            #summary of 4 lines from wikipedia 
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
            
        elif "which day it is" in query:
            tellDay()
            continue
            
        elif "tell me the time" in query:
            tellTime()
            continue
            
        elif "bye" in query:
            speak("Bye.")
            exit()
        
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop assistant")


if __name__ == '__main__':

    #main method for executing the functions
    Take_query()


        




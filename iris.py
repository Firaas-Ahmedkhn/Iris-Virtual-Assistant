import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import time
import requests
from datetime import date

# Getting date
my_date = date.today()
 
# Getting time
timestamp = time.strftime("%H: %M")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)

    engine.runAndWait()
speak("Hi, I am iris. Your Virtual Assistant. Please tell me how may I help you?")
print("Hi, I'm Iris . Your Virtual Assistant. Please tell me how may I help you?")

    

def takeCommand():
    '''Takes microphone input from user'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1       
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")    

    except Exception as e:
        speak("Please say that again...")
        return "None"
        
    return query

def Weather():
    '''Returns weather'''
    city = 'Aligarh'
    api_key = '2a4d09d3290b703880ae4903f2e4b956'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()
    weather_desc = data['weather'][0]['description'].capitalize()
    
    return weather_desc


is_on = True

if __name__ == "__main__":
    while is_on:
        query = takeCommand().lower()

        if "hi iris" in query:
            speak("Hi..")

        elif 'how are you' in query:
            speak("I am good. How are you?")

        elif "what's your name?" in query:
            speak("I am Iris. Your virtual assistant. From telling time and weather to search anything, I can do pretty much everything")    

        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open linkedin' in query:
            speak("Opening linkedin")
            webbrowser.open("https://www.linkedin.com/feed/")    

        elif 'open chat gpt' in query:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")
        
        elif 'open github' in query:
            speak("Opening github")
            webbrowser.open("https://github.com/")    

        elif 'open get hub' in query:
             speak("Opening github")
             webbrowser.open("https://github.com/")    

        elif 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("https://open.spotify.com/")    
            

        elif 'turn off' in query:
            speak("Turning off")
            is_on = False
        
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'time' in query:
            speak(f"It's {timestamp} sir")

        elif 'weather' in query:
            speak(f"Today's weather is {Weather()}")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox") 

        elif 'date today' in query:
            speak(f"Today is {my_date}")

        elif 'in youtube' in query:
            query = query.replace("youtube search", "")
            query = query.replace("iris", "") 
            query = query.replace("in youtube", "")
            query = query.replace("search", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("Searching in youtube...")   

        elif 'in google' in query:
            query = query.replace("in google", "")
            query = query.replace("iris", "")
            query = query.replace("search", "")
            query = query.replace("google search", "")
            web1 = "https://www.google.com/search?q="  + query
            webbrowser.open(web1)
            speak(f"Searching {query} in google...")

        elif 'in spotify' in query:
            query = query.replace("search spotify", "")
            query = query.replace("in spotify", "")
            query = query.replace("iris", "")
            web2 = "https://open.spotify.com/search/" + query 
            webbrowser.open(web2) 
            speak(f"Searching {query}in spotify...")   
    
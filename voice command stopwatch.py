import pyttsx3                         # install pyttsx3 tkinter using pip command
import speech_recognition as sr        # install speech_recognition using pip command
import datetime
from tkinter import *                  # install tkinter using pip command
from tkinter.font import Font
from datetime import datetime
import time
from threading import Thread 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    #speak("I am friday Sir. Please tell me how         can            I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")
        query = 'Nothing'
        return "None"
    return query


counter=66600

def stopwatch():
    def DClock():
            global counter
            global c
            try:     
                tt = datetime.fromtimestamp(counter)
                curr_time= tt.strftime(" %H:%M:%S ")
                clock.config(text=(curr_time))
                clock.after(1000,DClock)
                    
                if c=='start':
                    counter+=1

                if c=='stop':
                    pass
                        
                if c=='quit stopwatch':
                    command=window.quit()
                    c='stop'
                    query='reset' 
                    
                        

            except Exception as e:
                pass
                    
                

    window = Tk()
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight() 

    awidth =862
    aheight =496

    x=(width/2) - (awidth/2)
    y=(height/2) - (aheight/2)

    window.geometry(f'{awidth}x{aheight}+{int(x)}+{int(y)}')#"%dx%d"%(width,height))#"1300x400")
    window.title("stopwatch")

    message= Label(window, font=("Algerian",100,"italic"), text=(" STOPWATCH  "), fg="red",bg='green') #arial 
    message.grid(row=0,column=0)


                                            
    clock= Label(window, font=("times",150,"bold"),fg="black",bg='blue') #250
    clock.grid(row=1,column=0)

    design= Label(window, font=("Algerian",70), text=" *+*+*+*+\/+*+*+*+* ", fg="red",bg='green') #,"italic"
    design.grid(row=3,column=0)
        

    DClock()
    """    
    if __name__ == '__main__':
        print("f1")
        Thread(target = f1).start()"""
        

    window.mainloop()


def f1():
    print("say stopwatch")
    speak("say stopwatch")
    global counter
    global c

    while True:
        global c
        query = takeCommand().lower()

        if query=='stop':
            c='stop'
            print('stoped')
            speak('stoped')


        if query=='start':
            c='start'
            print('started')           
            speak('started')

        if query=='stopwatch':
            try:
                if __name__ == '__main__':
                    Thread(target = stopwatch).start()
            except Exception as e:
                pass

        if query=='quit stopwatch':
            query = 'reset'
            if query=='reset':
                c='stop'
                counter=66600
            time.sleep(1)
            c='quit stopwatch'
            print("stopwatch quited")
            speak("stopwatch quited")
            break

        if query=='reset':
            c='stop'
            counter=66600
            print("reseted")
            speak("reseted")
        
        else:
            pass


a = 1
if a==1:
    #print(wishMe())
    while True :
        print("one")
        speak('one')
        query = takeCommand().lower()

        if query=='1':
            f1()
            

        if query=='tu':
            print('hello')
            speak('hello')






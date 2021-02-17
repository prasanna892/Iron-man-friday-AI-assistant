import pyttsx3 # alredy installed
import speech_recognition as sr # alredy installed
import datetime
import wikipedia # alredy installed
import webbrowser
import os
import smtplib # alredy installed
import pywhatkit as kit # alredy installed
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login("prasannarajraj20799@gmail.com",'pra1san2na3')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am friday Sir. Please tell me how may I help you")       


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
        return ""
    return query


a = 1
if a==1:
    print(wishMe())
    while True :
        print("to activate please tell the password")
        speak("to activate please tell the password")
        query = takeCommand().lower()
        if 'wake up' in query:
            print("i am on sir ,,,,, please tell me what can i do for you sir ? ")
            speak("i am on sir ,,,,, please tell me what can i do for you sir ? ")

            while True:
            
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=5)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    
                elif 'open youtube' in query:
                    webbrowser.open("https//www.youtube.com")

                elif 'search youtube for' in query :
                    # voice command "search youtube for " (what you want to search)
                    query = query.replace('friday',"")
                    query = query.replace('for',"")
                    query = query.replace('search',"")
                    query = query.replace('youtube',"")
                    query = query.replace('video',"")
                    query = query.replace('song',"")
                    #a='ok sir , searching',query,'in youtube'
                    print('ok sir , searching',query,'in youtube')
                    speak(a)
                    kit.playonyt(query)

                elif 'open google' in query:
                    webbrowser.open("https://www.google.com")

                elif 'open mozilla firefox' in query:
                    path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    # add your firefox path
                    os.startfile(path)   

                elif 'play music' in query:
                    music_dir = 'D:\\song'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif query=='what the time' or query=="what's the time" or query=="what is the time":
                    strTime = datetime.datetime.now().strftime("%I:%M  %p")    
                    print(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")

                elif query=='what the day' or query=="what's the day" or query=="what is the day":
                    strTime = datetime.datetime.now().strftime("%A")
                    print(f"Sir, the day is {strTime}")
                    speak(f"Sir, the day is {strTime}")
                
                elif query=='what the year' or query=="what's the year" or query=="what is the year":
                    strTime = datetime.datetime.now().strftime("%y")
                    print(f"Sir, the year is 20 {strTime}")
                    speak(f"Sir, the year is 20 {strTime}")

                elif query=='what the year format' or query=="what's the year format" or query=="what is the year format":
                    strTime = datetime.datetime.now().strftime("%d-%B-%Y")
                    print(f"Sir, the year is {strTime}")
                    speak(f"Sir, the year is {strTime}")

                elif 'email to' in query:
                    email_list = {'first mail':"k.prasanna08092002@gmail.com",'second mail':"e.thulasirajan@gmail.com"}
                    speak("ok sir     to whom you want to sent the email")
                    print("for prasanna say,,,,,,,,,,,,,,first mail")
                    speak("for,,,,,,,,,,,,,,,, prasanna,,,,,,,,,,,say,,,,,,,,,,first mail ,,,,,,,,,,,,,,")
                    print("for thulasi rajan say,,,,,,,,second mail")
                    speak("for,,,,,,,,,,,,,, thulasi rajan ,,,,,,,,,,,say,,,,,,,,second mail,,,,,,,,,,,or")
                    print('no one')
                    speak('no one')
                    name = takeCommand().lower()
                    receiver = email_list.get(name,'')

                    while True:
                        
                        if receiver == 'k.prasanna08092002@gmail.com'  or receiver == 'e.thulasirajan@gmail.com' :
                            print('receiver = ', receiver )
                            try:
                                print('What is the subject of your email?')
                                speak('What is the subject of your email?')
                                print("if your mail subject is ok. please say     subject ok")
                                speak("if your mail subject is ok. please say,,,,,,,,,,,,,subject ok")
                                sub = []
                                for i in range(9999999999):
                                    su = takeCommand()
                                    sub.append(su)
                                    if 'subject ok' in su:
                                        print('your subject is confirmed')
                                        speak('your subject is confirmed')
                                        sub.remove('subject ok')
                                        subject = ' '.join(sub)
                                        break
                                print("your subject is :")
                                speak('your subject is')
                                print('       ',subject)


                                #speak('What is the subject of your email?')
                                #subject = takecommand

                                print('What is the message of your email?')
                                speak('What is the message of your email?')
                                print("if your mail message is ok. please say       message ok")
                                speak("if your mail message is ok. please say,,,,,,,,,,,,,message ok")
                                mes = []
                                for i in range(9999999999):
                                    me = takeCommand()
                                    mes.append(me)
                                    if 'message ok' in me:
                                        print('your message is confirmed')
                                        speak('your message is confirmed')
                                        mes.remove('message ok')
                                        message = ' '.join(mes)
                                        break
                                print("your message is :")
                                speak('your message is')
                                print('       ',message)


                                #speak('what is the message of your email?')
                                #message = takeCommand()


                                print("do you want to sent this mail ? say yes or no ?")
                                speak("do you want to sent this mail ?        say         yes     or      no        ? ")
                                query = takeCommand().lower()
                                if "yes" in query:
                                    print('mail sending please wait')
                                    speak('mail sending please wait')
                                    send_email(receiver, subject, message)
                                    print('Your email has been sented sir')
                                    speak('Your email has been sented sir')
                                    break
                                elif "no" in query:
                                    print('Your email cancelled sir')
                                    speak('Your email cancelled sir')
                                    break
                                                    
                            except Exception as e :
                                print(e)
                                print("sorry sir      the email has not been send       due to some error")
                                speak("sorry sir      the email has not been send       due to some error")
                                break

                        if 'no one' in query:
                            print("ok sir no one  selected ")
                            speak("ok sir no one  selected ")
                            break
                        print("no mail is selected sir .please say again        email to")
                        speak("no mail is selected sir ,,,,,,,,please say again,,,,,,,,,,,email to ")
                        break   
                    
                elif query == 'quit' or query == 'quite':
                    print("quitting sir")
                    speak("quitting sir")
                    break

                #add voice to type program
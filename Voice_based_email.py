#Name : Gaurav Antal
#Section : G
#University Roll number : 2014660
#Mini-Project : voice based mail

import datetime
# A date in python is not a data type of its own, can import a module named datetime to work with dates as date object.
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine_on = pyttsx3.init()
voices = engine_on.getProperty('voices')
#engin_start.setProperty('voice',voices[1].id)  this is for female voice


def say(text):
    engine_on.say(text)
    engine_on.runAndWait()

def today():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                        say("good morning sir")

            elif hour >=12 and hour < 18:
                        say("good afternoon sir")

            else:
                        say("good evening sir")

            say("I am your personal assistant antlaa")

def request_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('myemailaddressisantal@gmail.com', 'Guruji19021302#@.Gsg')
    email = EmailMessage()
    email['From'] = 'myemailaddressisantal@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {

    'gaurav' : 'goluantal99@gmial.com',
    'anchal': 'aanchalantal@gmail.com',
    'narendra': 'narendraantal@gmail.com',
    'lakshya' : 'shersiaguruji@gmail.com'
}


def request_email_info():
    say('To Whom you want to send email')
    try:
        key = request_info()
        value_email = email_list[key]
    except:
        say("name not found sir")
        return 0



    print(value_email)
    say('What is the subject of your email?')
    subject = request_info()
    say('Tell me the text in your email')
    message = request_info()
    send_email(value_email, subject, message)
    say('Hey . Your email is sent')
    say('Do you want to send more email?')
    send_more = request_info()
    if 'yes' in send_more:
        request_email_info()

today()
request_email_info()
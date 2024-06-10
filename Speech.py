import tkinter as tk
from tkinter import Message ,Text
from tkinter import*
import os

import speech_recognition as sr
from lxml import html
import requests
import os
import pygame
import random
import time

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import nltk
nltk.download('punkt')
# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf

import random

import json
import TrainModel
import chat
import pyttsx3
import webbrowser
import googlesearch




window = tk.Tk()
window.title("Teaching Assistant")

 
window.geometry('1280x720')
window.configure(background='indigo')
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Virtual Teaching Assistant" ,bg="indigo"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'roman underline')) 
message1.place(x=100, y=20)

lbl = tk.Label(window, text="You Said",width=20  ,height=2  ,fg="white"  ,bg="Red" ,font=('times', 15, ' bold ') ) 
lbl.place(x=100, y=150)

txt = Text(window, width = 30, height = 3, wrap = WORD,bg="white",fg="red",font=('times', 15, ' bold '))
txt.place(x=400, y=150)

lbl2 = tk.Label(window, text="Chat Bot Reply",width=20  ,fg="white"  ,bg="red"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=100, y=300)

txt1 = Text(window, width = 30, height = 3, wrap = WORD,bg="white",fg="red",font=('times', 15, ' bold '))
txt1.place(x=400, y=300)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="white"  ,bg="red"  ,height=2 ,font=('times', 15, ' bold ')) 
lbl3.place(x=100, y=440)

txt2 = Text(window, width = 30, height = 2, wrap = WORD,bg="white",fg="black",font=('times', 15, ' bold '))
txt2.place(x=400, y=440)


txt3 = Text(window, wrap = NONE,width = 40, height = 15, bg="white",fg="red",font=('times', 15, ' bold '))


vscroll = Scrollbar(window, orient=VERTICAL, command=txt3.yview)
txt3['yscroll'] = vscroll.set

vscroll.pack(side="right", fill="y")
txt3.pack(side="left", fill="both", expand=True)

txt3.place(x=800, y=150)



#mytext = 'Welcome System!'
#language = 'en'
#myobj = gTTS(text=mytext, lang=language, slow=False) 
#myobj.save("welcome.mp3") 
  
# Playing the converted file 


#pygame.mixer.init()
#pygame.mixer.music.load('welcome.mp3')
#pygame.mixer.music.play()
#while pygame.mixer.music.get_busy(): 
 #   pygame.time.Clock().tick(100)
#pygame.quit()


def clear():
    print("Clear1")
    txt.delete(0.0, END)
    txt1.delete(0.0, END)
    txt2.delete(0.0, END)
    txt3.delete(0.0, END)
    
def StartChat():
    txt.delete(0.0, END)
    txt1.delete(0.0, END)
    txt2.delete(0.0, END)
    #txt3.delete(0.0, END)
    language = 'en'
    r = sr.Recognizer()
    with sr.Microphone() as source:
    	r.adjust_for_ambient_noise(source, duration = 1)
    	print("hey!! Ask me something ")
    	audio = r.listen(source)
         

    	
    try:
            t=r.recognize_google(audio)
            print ("You just said " +t)
            txt.insert(END, t)
            txt3.insert(END, "\n\nYour Chat>>>" + t)
            ent=chat.classify(t)
            for n in ent:
            	print(n[0])
            	txt2.insert(END,n[0]+",")
            	reply=chat.response(t)
            	txt1.insert(END,reply)
            	txt3.insert(END, "\nChat Bot Reply>>>" + reply)
            	engine = pyttsx3.init()
            	engine.say(reply)
            	engine.runAndWait()
   
    except sr.UnknownValueError:
            print("Sorry!... I Can't understand ")
            loopme=1
            txt2.insert(END, "Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            txt2.insert(END, "Could not request results from Google Speech Recognition service;")
            
    #while(1):
    #	ques = raw_input("hey!! Ask me something -: ")
    #	print(ques)
    #	print(chat.classify(ques))
    #	chat.response(ques)

      
def train():
    TrainModel.Train()
    res = "Finished Data Train"
    txt2.insert(END, res)

#loginWindow = tk.Button(window, text="login", command= webbrowser.open_new(r"http://127.0.0.1:8000/")  ,fg="white"  ,bg="red"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
#loginWindow.place(x=1000, y=540)

#loginWindow = tk.Button(window, text="Login", command=webbrowser.open_new(r"http://127.0.0.1:8000/")  ,fg="white"  ,bg="blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
#loginWindow.place(x=1000, y=540)


traindata = tk.Button(window, text="Train Data", command=train  ,fg="white"  ,bg="blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
traindata.place(x=100, y=540)	

st = tk.Button(window, text="Start Chat", command=StartChat  ,fg="white"  ,bg="blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
st.place(x=400, y=540)

  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg="blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=700, y=540)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="blue"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=540)


window.mainloop()




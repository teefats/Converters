from tkinter import *
from gtts import gTTS
from playsound import playsound

#Initialise the window(Interacting with the wondow)
root =Tk()
root.geometry("350x300")
# root.resizable(0,0)
root.configure(bg="ghost white")
root.title("Yoruba - Text To Speech")
#Heading
Label(root, text = 'TEXT_TO_SPEECH' , 
font = 'arial 20 bold' , bg = "white smoke").pack()
Label(root, text = 'Tunde' , 
font = 'arial 20 bold' , bg = "white smoke",width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

from tkinter import Tk, Label, Entry, Button, StringVar
from gtts import gTTS
from playsound import playsound

root = Tk()

root.geometry('350x350')
root.configure(bg='ghost white')
root.title('TEXT TO SPEACH')

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

def TTS():
	message = entry_field.get()
	speech = gTTS(text = message)
	speech.save('TTS.mp3')
	playsound('TTS.mp3')

def Reset():
	Msg.set('')

Button(root, text = "PLAY", font = 'arial 15 bold' , command = TTS ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)


root.mainloop()
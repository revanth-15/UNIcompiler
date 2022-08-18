import pygame
from pygame import mixer
from tkinter import*
import os
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()
root=Tk()
root.title('MP3 Music player')
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('optima',15),width=50,height=15)
playlist.grid(columnspan=20)
os.chdir(r'E:\certificates\Internship\UniCompiler\Songs')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('candara',20),bg="white",fg="green",padx=2,pady=0)
playbtn.grid(row=1,column=0)
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('candara',20),bg="white",fg="blue",padx=2,pady=0)
pausebtn.grid(row=1,column=1)
stopbtn=Button(root,text="stop",command=stopsong)
stopbtn.config(font=('candara',20),bg="white",fg="red",padx=2,pady=0)
stopbtn.grid(row=1,column=2)
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('candara',20),bg="white",fg="orange",padx=2,pady=0)
Resumebtn.grid(row=1,column=3)
mainloop()

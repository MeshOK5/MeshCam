#Libraries
from tkinter import *
import pyaudio
import audioop
import math
from os import abort
from device_function import choice_device
from color_function import choice_color

p = pyaudio.PyAudio()

#User choose device
device = choice_device(p)

#User choose color
color = choice_color(p)

#Create window
win = Tk()
win.title("MeshTuber")
win.geometry("200x180")
win.config(background=color)
win.resizable(False, False)

#Set icon
icon = PhotoImage(file="images/icon.png")
win.iconphoto(False, icon)

#Load images
first_pose = PhotoImage(file="images/Not_speaker.png")
second_pose = PhotoImage(file="images/Speaker.png")
third_pose = PhotoImage(file="images/Close.png")

#Create avatar label
avatar = Label(win, image=first_pose, background=color)
avatar.pack(pady=10)

#Some data
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

#Create stream
try:
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=device)
except Exception as ex:
    print(ex)
    abort()

count = 0

def audio_catcher():
    global avatar
    global first_pose
    global second_pose
    global third_pose
    global count

    #Grab audio from the device that user choose
    data = stream.read(CHUNK, 
                       exception_on_overflow=False)
    try:

        #Check decibel from microphone
        rms = audioop.rms(data, 2)
        decibel = 20 * math.log10(rms)

        #if decibel < 49.5 change Avatar image to First_pose
        if decibel < 49.5:
            count += 1

            #if remainder from Count = 0 change Avatar image to Third_pose
            if count % 100 == 0:
                avatar.config(image=third_pose)
                count = 0
            else:
                avatar.config(image=first_pose)

        #if decibel >= 49.5 change Avatar image to Second_pose
        else:
            avatar.config(image=second_pose)
    except:
        None
    win.after(35, audio_catcher)

#Main loop
win.after(0, audio_catcher)
win.mainloop()
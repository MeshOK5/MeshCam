#Libraries
from pyaudio import *
from os import abort

#User choose color function
def choice_color(p:PyAudio) -> str:
    colors = ["green", "blue", "purple"]
    color = input("What color will be a background?(green, blue or purple): ")
    if color.lower() in colors:
        return color
    else:
        print("Unacceptable color")
        abort()
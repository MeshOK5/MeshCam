#Libraries
from pyaudio import *
from os import abort

#Print all devices function
def get_devices(p:PyAudio) -> None:
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)["name"])

#User choose device function
def choice_device(p:PyAudio) -> int:
    get_devices(p)
    try:
        device = int(input("Enter your microphone index: "))
    except Exception as ex:
        print(ex)
        abort()
    return device
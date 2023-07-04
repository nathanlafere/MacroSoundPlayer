import time
from pygame import mixer
import keyboard
from tkinter.filedialog import askopenfilename
import os


# Dependecie of VB-CABLE Virtual Audio Device.
# download at https://vb-audio.com/Cable/ or change the device in the mixer.init

def play_sound(file):
    mixer.init(devicename= 'CABLE Input (VB-Audio Virtual Cable)')    
    mixer.music.load(file) # Load the mp3
    mixer.music.play() # Play it
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

def create_hotkey():    
    print("Choose the mp3 file!")
    file = askopenfilename()
    if file == '':
        prompt_text()
        return
    print(f"-=-= {file} =-=-")
    while True:
        hotkey = input("Enter the key to bind (Ex. shift+1): ")
        if input(f'Are you sure you want to use {hotkey} as a hotkey? (y/n) ')[0].lower() == 'y':
            break
    hotkey_list.append([hotkey,file[file.rfind('/')+1:]])
    prompt_text()
    keyboard.add_hotkey(hotkey, lambda: play_sound(file))
    
def prompt_text():
    print('ctrl+alt+1 = new hotkey', end='')
    for _hotkey in hotkey_list:
        print(f' || {_hotkey[0]} = {_hotkey[1]}', end='')
    print()

hotkey_list = []
prompt_text()
keyboard.add_hotkey("ctrl+alt+1", create_hotkey)
keyboard.wait('esc')
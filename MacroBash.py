import time
from pygame import mixer
import keyboard
from tkinter.filedialog import askopenfilename
import os

def play_sound(file):
    mixer.init(devicename= 'CABLE Input (VB-Audio Virtual Cable)')    
    mixer.music.load(file) # Load the mp3
    mixer.music.play() # Play it
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

def config_new_hotkey():    
    print("Choose the mp3 file!")
    file = askopenfilename()
    if file == '':
        prompt_text()
        return
    print(f"-=-= {file} =-=-")
    while True:
        hotkey = input("Enter the key to bind (Ex. shift+1): ")
        if input(f'Are you sure you want to use {hotkey} as a hotkey? (y/n) ')[:1].lower() == 'y':
            break
    os.system('copy '+file.replace("/","\\")+f' {os.getcwd()}\SoundFiles\\'+file[file.rfind('/')+1:file.rfind('.mp3')]+f'_{hotkey.replace("+","-")}.mp3')
    hotkey_list.append([hotkey,file[file.rfind('/')+1:file.rfind('.mp3')],file])
    prompt_text()
    create_hotkey(hotkey, file)

def create_hotkey(hotkey,file):
    keyboard.add_hotkey(hotkey, lambda: play_sound(file))

def load_hotkey():
    for file in os.listdir(os.getcwd()+'\SoundFiles'):
        hotkey_list.append([file[file.rfind('_')+1:file.rfind('.mp3')].replace("-","+"),file[:file.rfind('_')],os.getcwd()+'\SoundFiles\\'+file])
        create_hotkey(hotkey_list[-1][0],hotkey_list[-1][2])

def prompt_text():
    print('ctrl+alt+1 = new hotkey', end='')
    for _hotkey in hotkey_list:
        print(f' || {_hotkey[0]} = {_hotkey[1]}', end='')
    print()

hotkey_list = []
load_hotkey()
prompt_text()
keyboard.add_hotkey("ctrl+alt+1", config_new_hotkey)
keyboard.wait('esc')
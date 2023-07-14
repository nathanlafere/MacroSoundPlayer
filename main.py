import time
from pygame import mixer
import keyboard
import os


# Dependecie of VB-CABLE Virtual Audio Device.
# download at https://vb-audio.com/Cable/ or change the device in the mixer.init

def play_sound(file,checkvar):
    if interface is None or checkvar.get() != 0:
        mixer.init(devicename= 'CABLE Input (VB-Audio Virtual Cable)')    
        mixer.music.load(file) # Load the mp3
        mixer.music.play() # Play it
        while mixer.music.get_busy() and not keyboard.is_pressed('esc'):  # wait for music to finish playing
            continue
        mixer.quit()

def create_new_hotkey(hotkey,file):    
    hotkey = keyboard._canonical_names.normalize_name(hotkey)
    new_path = f'{os.getcwd()}\\'+file[file.rfind('/')+1:file.rfind('.mp3')]+f'_{hotkey.replace("+","-")}.mp3'
    os.system('copy '+file.replace("/","\\")+f' {new_path}')
    hotkey_list.append([hotkey,file[file.rfind('/')+1:file.rfind('.mp3')],new_path])
    start_hotkey(hotkey, new_path)

def start_hotkey(hotkey,file):
    keyboard.add_hotkey(hotkey[0], lambda: play_sound(file,hotkey[-1]))

def load_hotkeys():
    for hotkey in hotkey_list:
        start_hotkey(hotkey,hotkey[2])

def start_load_hotkeys():
    for file in os.listdir(os.getcwd()):
        hotkey_list.append([file[file.rfind('_')+1:file.rfind('.mp3')].replace("-","+"),file[:file.rfind('_')],os.getcwd()+'\\'+file])
        start_hotkey(hotkey_list[-1],hotkey_list[-1][2])

os.chdir(os.getcwd()+'\SoundFiles')
hotkey_list = []
interface = None
start_load_hotkeys()

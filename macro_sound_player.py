import time
from pygame import mixer
import keyboard

# Dependecie of VB-CABLE Virtual Audio Device.
# download at https://vb-audio.com/Cable/ or change the device in the mixer.init

def play_sound(file):
    mixer.init(devicename= 'CABLE Input (VB-Audio Virtual Cable)')    
    mixer.music.load(file) # Load the mp3
    mixer.music.play() # Play it
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

keyboard.add_hotkey("shift+1", lambda: play_sound("SoundFiles\\anchor.mp3"))
keyboard.wait()
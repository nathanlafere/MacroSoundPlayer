import main
import keyboard
from tkinter.filedialog import askopenfilename
import os

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
    main.hotkey_list.append([hotkey,file[file.rfind('/')+1:file.rfind('.mp3')],file])
    prompt_text()
    create_hotkey(hotkey, file)

def create_hotkey(hotkey,file):
    keyboard.add_hotkey(hotkey, lambda: main.play_sound(file))

def prompt_text():
    print('ctrl+alt+1 = new hotkey', end='')
    for _hotkey in main.hotkey_list:
        print(f' || {_hotkey[0]} = {_hotkey[1]}', end='')
    print()

prompt_text()
keyboard.add_hotkey("ctrl+alt+1", config_new_hotkey)
keyboard.wait()
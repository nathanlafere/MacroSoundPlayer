from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import main

def ask_path():
    file = askopenfilename()
    path_entry.insert(0,file)

def reload_inside_canvas_frame():
    main.load_hotkeys()
    for child in inside_canvas_frame.winfo_children():
        child.destroy()
    for hotkey in main.hotkey_list:
        create_grid(hotkey)
    my_canvas.configure(scrollregion=my_canvas.bbox("all"))

def del_hotkey(hotkey):
    if not main.mixer.get_init():
        main.hotkey_list.remove(hotkey)
        os.system(f"del {hotkey[2]}")
        main.keyboard.clear_all_hotkeys()
        reload_inside_canvas_frame()

def create_hotkey():
    if path_entry.get() != '' and hotkey_entry.get() != '':
        main.create_new_hotkey(hotkey_entry.get(),path_entry.get())
    reload_inside_canvas_frame()

def create_grid(_hotkey):
    if len(_hotkey) == 4:
        Checkbutton(inside_canvas_frame,variable = _hotkey[3]).grid(row=1 + main.hotkey_list.index(_hotkey), column=0)
    else:
        CheckVar = IntVar()
        Checkbutton(inside_canvas_frame,variable = CheckVar).grid(row=1 + main.hotkey_list.index(_hotkey), column=0)
        _hotkey.append(CheckVar)
    Label(inside_canvas_frame, text=f'{_hotkey[1]} {_hotkey[0]}',font=("Tekton Pro",10),wraplength=155,justify="center").grid(row=1 + main.hotkey_list.index(_hotkey), column=1)
    new_key_entry = Entry(inside_canvas_frame,background="#595959",fg="white", width=17)
    new_key_entry.grid(row=1 + main.hotkey_list.index(_hotkey), column=2,padx=3)
    Button(inside_canvas_frame, text="Change",font=("Tekton Pro",10), command= lambda: change_hotkey(_hotkey,new_key_entry.get())).grid(row=1+main.hotkey_list.index(_hotkey),column=3,padx=3)
    Button(inside_canvas_frame, text="Delete",font=("Tekton Pro",10), command= lambda: del_hotkey(_hotkey)).grid(row=1+main.hotkey_list.index(_hotkey),column=4,padx=3)
    
def change_hotkey(_hotkey, new_key):
    if not main.mixer.get_init():
        os.system('ren '+_hotkey[2][_hotkey[2].rfind("\\")+1:]+' '+_hotkey[2][_hotkey[2].rfind("\\")+1:_hotkey[2].rfind("_")+1]+new_key.replace("+","-")+'.mp3')
        main.hotkey_list[main.hotkey_list.index(_hotkey)][0] = new_key
        main.hotkey_list[main.hotkey_list.index(_hotkey)][2] = _hotkey[2][_hotkey[2].rfind("\\")+1:_hotkey[2].rfind("_")+1]+new_key.replace("+","-")+'.mp3'
        main.keyboard.clear_all_hotkeys()
        reload_inside_canvas_frame()
    
window = Tk(className=" Macro Sound Player")
window.geometry("600x400")
window.configure(bg="#595959")
window.resizable(width=FALSE, height=FALSE)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)
tittle = Label(text="Macro Sound Player",fg="white",bg="gray",font=("Times", "24", "bold italic"),width=50,relief="groove",highlightbackground="gray",highlightthickness=1.5)
tittle.grid(row=0,column=0,columnspan=3)

frame1 = Frame(window,bg="gray", padx=10, pady=10)
frame1.grid(row=1,columnspan=4,pady=8)

hotkey_entry = Entry(frame1,background="#595959",fg="white", width=17)
hotkey_entry.insert(0,"shift+1")
hotkey_entry.grid(row=1,column=1,padx=3)
path_entry = Entry(frame1,background="#595959",fg="white", width=50)
path_entry.grid(row=1,column=2,padx=3)
Button(frame1, text="path", font=("Tekton Pro",10),command=ask_path).grid(row=1,column=3,padx=3)
Button(frame1, text="Confirm", font=("Tekton Pro",10), command=create_hotkey).grid(row=1,column=4,padx=3)

collection_frame = Frame(window,bg="gray")
my_canvas = Canvas(collection_frame,)
my_canvas.grid(rowspan=7,columnspan=7,padx=3,pady=3)
collection_frame.grid(row=2)
scrollbar = Scrollbar(collection_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.grid(column=7,row=0,rowspan=7,sticky=N+S+W)
my_canvas.configure(yscrollcommand=scrollbar.set,width=430, height=272)
my_canvas.bind('<Configure>',  lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
inside_canvas_frame = Frame(my_canvas,padx=5)
my_canvas.create_window((0,0),window=inside_canvas_frame, anchor="nw")

for hotkey in main.hotkey_list:
    create_grid(hotkey)

window.mainloop()

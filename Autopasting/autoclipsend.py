from pynput import keyboard
import pyperclip
import tkinter
from tkinter import filedialog
import pathlib

pressed_key=set()
clip_content=''
file_path=''

def press(k):
    global clip_content
    pressed_key.add(k)
    if keyboard.Key.ctrl in pressed_key and keyboard.KeyCode(char='c') in pressed_key:
        print(f"disured key is pressed")
        clip_content= pyperclip.paste()
        print(f"clip:{clip_content}")    
    
def send_dialogue(k):
    global file_path
    try:
        if keyboard.Key.ctrl in pressed_key and keyboard.KeyCode(char='m') in pressed_key:
            if len(file_path) == 0:    
                root=tkinter.Tk()
                root.withdraw()
                file_path=filedialog.askopenfilename(
                    title="select Obsidian note",
                    filetypes=[("Markdown files","*.md")])
                root.destroy()

            print(f"path:{file_path}---content:{clip_content}")

            with open(file_path,"a",encoding="utf-8") as file:
                file.write(f"{clip_content}\n")

    except KeyError:
        pass    

def combine_func(k):
    press(k)
    send_dialogue(k)
    print(file_path)

def release(k):
    try:
        pressed_key.remove(k)
    except KeyError:
        pass    

with keyboard.Listener(on_press=combine_func,on_release=release) as listener:
    listener.join()

#with keyboard.Listener(on_press=send_dialogue) as listener:
#    listener.join()






# Import module
import os
os.system('pip install wmi requests')
import wmi
import json
import requests
import os.path

# import everything from tkinter module
from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox

#creating tkinter root window
# Initializing the wmi constructor
f = wmi.WMI()
def run():
    with open("program.name","r") as f_read:
        program_read = f_read.read()
        f_read.close()
    while True:
        flag = 0
        root = tkinter.Tk()
        root.attributes("-topmost", True)


        def get_Quote():
            response = requests.get("https://zenquotes.io/api/random")
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " -" + json_data[0]['a']
            return (quote)


        # Iterating through all the running processes
        for process in f.Win32_Process():
            if program_read == process.Name:
                tkinter.messagebox.showinfo("ProcrastinatorMotivator",
                                            f"While you are procastinating someone else is working hard to obtain your postion. {get_Quote()}")
                flag = 1
                break

        if flag == 0:
            print("Application is not Running")
        root.destroy()
        root.mainloop()
 
def open_file():
    program_name=program_var.get()
    with open("program.name", "w") as file:
        file.write(program_name+'.exe')
        file.close()
    win_startup.destroy()
    run()
if os.path.exists("program.name") == True:
    run()

else:
    global win_startup
    win_startup=tkinter.Tk()
    win_startup.geometry("400x250")
    program_var = tkinter.StringVar()
    program_instruction=Label(win_startup, text="Name of the program that you'd like to block:").grid(row=0, column=0)
    program = Entry(win_startup,textvariable=program_var).grid(row=0, column=1)
    sub_btn=Button(win_startup, text='Go!', command=open_file).grid(row = 4, column = 0)
    win_startup.mainloop()



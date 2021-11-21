# Import module
import os
os.system('pip install -r requirements.txt')
import wmi
import json
import requests
import os.path

# import everything from tkinter module
from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox

# create a tkinter root window




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
if os.path.exists("program.name") == True:
    run()
else:
    program = input("The name of the program you would like to block: ")
    with open("program.name", "w") as file:
        file.write(program)
        file.close()
    run()


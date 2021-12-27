# Import module
import os
os.system('pip install psutil requests')
import psutil
import json
import requests
import os.path
import getpass
# import everything from tkinter module
from tkinter import *

# import messagebox from tkinter module
import tkinter.messagebox
import shutil
# creating tkinter root window
# Initializing the wmi constructor
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def run():
    with open("program.name","r") as f_read:
        program_read = f_read.read()
        f_read.close()
    while True:
        flag = 0
        root = tkinter.Tk()
        root.attributes("-topmost", True)


        def get_Quote():
            #getting the quote
            response = requests.get("https://zenquotes.io/api/random")
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " -" + json_data[0]['a']
            return (quote)
        # Check if any chrome process was running or not.
        if checkIfProcessRunning(program_read):
            tkinter.messagebox.showinfo("ProcrastinatorMotivator",
                                            f"While you are procastinating someone else is working hard to obtain your postion. {get_Quote()}")

        else:
            print('')

        
        root.destroy()
        root.mainloop()
def createStartup():
    user=getpass.getuser()
    original = 'ProcastinatorMotivator.exe'
    target = "C:/Users/"+ user + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"+original
    shutil.copyfile(original, target)
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
    startup_btn=Button(win_startup, text='Add to Startup', command=createStartup).grid(row = 4, column = 1)
    win_startup.mainloop()



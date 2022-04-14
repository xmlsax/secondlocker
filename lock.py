import tkinter as tk
import abort, os

try: 
    try:
        f = open('C:\\xmlsax\\secondlocker\\defaultpasswordlocation')
        passwordl =  f.read()
        f.close()
    except (FileNotFoundError, PermissionError):
        passwordl = 'C:\\xmlsax\\secondlocker\\defaultpassword'
    password = open(passwordl).read()
except (FileNotFoundError, PermissionError): 
    password = 'DefaultPassword'

win = tk.Tk()
win.attributes('-topmost', True)
win.attributes('-fullscreen', True)
win.config(background='blue')
def verify():
    if inputbox.get() == password: abort.abort()
inputbox = tk.Entry(win)
verifybt = tk.Button(win, text='Submit', command=verify)
inputbox.pack(side=tk.TOP, expand=True, fill=tk.X)
verifybt.pack(side=tk.LEFT)
win.mainloop()
os.system("shutdown -s -t 0")

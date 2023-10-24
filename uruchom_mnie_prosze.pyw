import ctypes
from time import sleep
import tkinter as tk
import threading


window = tk.Tk()
greeting = tk.Label(text="Let's play a game")
greeting.config(font=("Comic Sans MS", 44))
greeting.pack(padx=(50,50), pady=(50,50))

def loop():
    while True:
    
        try:
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
            sleep(1)
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
            sleep(1)
        except:
            continue
    
t = threading.Thread(target=loop)
t.start()

window.mainloop()

#import ctypes
import sys
import os
import tkinter as tkr
#from infi.systray import SysTrayIcon

#just to make sure that icon will be in .exe file
def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#root
app = tkr.Tk()

#window look
app.title('Overlay')
app.geometry("1080x910")
app.wm_attributes('-alpha',0.5,'-topmost',1)
app.configure(background='black')

#icon in the top left corner
app.iconbitmap(default=resource_path('icons8-window-shade-96.ico'))

'''
#text in tray menu
def say_hello(systray):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Operational!', 'Dark Window - status', 0)

    
#tray icon and hover text
menu_options = (("Status", None, say_hello),("Open", None, app))
menu_options = ()
systray = SysTrayIcon('icons8-window-shade-96.ico', 'Dark Window', menu_options)  
systray.shutdown()                                                     
systray.start()
'''

app.mainloop()
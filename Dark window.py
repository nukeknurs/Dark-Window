import tkinter as tkr 

#root
app = tkr.Tk()

#window look
app.title('Overlay')
app.geometry("1000x1000")
app.wm_attributes('-alpha',0.5,'-topmost',1)
app.configure(background='black')

#icon
app.iconbitmap(r'C:\Users\porto\Desktop\icons8-window-shade-96.ico')

app.mainloop()


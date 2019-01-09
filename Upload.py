# assuming Python3
from Tkinter import *
import subprocess as sub

WINDOW_SIZE = "600x400"

root = Tk()
root.geometry(WINDOW_SIZE)

app = Frame(root)
app.grid()#row=2, column=3, columnspan=2)

#Button1 = Button(app, text = "button A")
button1 = Button(app, text="UPLOAD FOLDER")
button1.grid(row=1, column=1)
button1.configure(command=lambda: sub.call('./Upload.sh'))#.pack() ###Opens file successfully!!!


#kick off the event loop
root.mainloop()
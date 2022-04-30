import tkinter
from tkinter import *
import pyscreenrec
import randomname
root = tkinter.Tk()
record = pyscreenrec.ScreenRecorder()
root.title("Screen Recorder")
root.geometry("400x600")
root.config( bg="#fff")
root.resizable(False, False)
photo = PhotoImage(file = "src/res/panda_logo.png")
root.iconphoto(False, photo)
var = StringVar()
label = Label( root, textvariable=var, font=('bold', 20), bg="#fff" )
var.set("Panda Screen Recorder")

#some background editing
bg_img = PhotoImage(file="src/res/kodak.png")
Label(root, image=bg_img, bg="#fff").place(x=-40, y=50)

label.pack()
a = randomname.get_name()
b = ".mp4"
c = a+b
def Start_rec():
    record.start_recording(a+".mp4", 5) 
def pause_rec():
    record.pause_recording()
def stop_rec():
    record.stop_recording()


# start_btn_img = PhotoImage(file='')
# stop_btn_img = PhotoImage(file="src/res/stop-circle-line.png")
# pause_btn_img = PhotoImage(file="src/res/pause-circle-fill.png")
start = Button(root,text="START",font=('times', 15), activebackground="#f1f1f1", command=Start_rec).place(x=130, y=450)
stop  = Button(root,text="STOP",font=('times', 15), activebackground="#f2f2f2", command=stop_rec).place(x=30, y=450)
pause = Button(root,text="Pause",font=('times', 15), activebackground="#f1f1f1",command=pause_rec).place(x=220, y=450)
resume = Button(root,text="Resume",font=('times', 15), activebackground="#f1f1f1").place(x=300, y=450)


root.mainloop()

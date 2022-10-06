import cv2
import tkinter as tk
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox, filedialog

# #GUI Designs================================================================================
# def widgets():
#     lab0 = Label(root, bg="steelblue", fg="white", text="Camera", font=20)
#     lab0.grid(row=1, column=1, pady=10, padx=10, columnspan=2)
#     global lab1
#     lab1 = Label(root, bg="steelblue", borderwidth=3, relief="groove")
#     lab1.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
#
#     en0 =Entry(root, width=55, textvariable=desPath)
#     en0.grid(row=3, column=1, pady=10, padx=10)
# #GUI Buttons================================================================================
#     btn0 = Button(root, text="Browse", width=10, command=desbrowse)
#     btn0.grid(row=3, column=2, padx=10, pady=10)
#
#     btn1 = Button(root, text="Capture", width=10, bg="lightblue", command=capture)
#     btn1.grid(row=4, column=1, pady=10, padx=10)
#     global btn2
#     btn2 = Button(root, text="Stop Cam", width=10, bg="lightblue", command=stop)
#     btn2.grid(row=4, column=2, padx=10, pady=10)
# #============================================================================================
#     lab2 = Label(root, text="Image Preview", bg="steelblue", fg="white", font=20)
#     lab2.grid(row=1, column=4, padx=10, pady=10, columnspan=2)
#
#     global lab3
#     lab3 = Label(root, bg="steelblue", borderwidth=3, relief="groove")
#     lab3.grid(row=2, column=4, pady=10, padx=10, columnspan=2)
#
#     en1 = Entry(root, width=55, textvariable=imgPath)
#     en1.grid(row=3, column=4, padx=10, pady=10)
#
#     btn3 = Button(root, width=10, text="Browse", command=desbrowse)
#     btn3.grid(row=3, column=5, pady=10, padx=10)
#
#     showfeed()
# #=============================================================================================

#WebCam=======================================================================================
def showfeed():

    ret, frame = root.cap.read()
    global lab1

    if ret:
        frame=cv2.flip(frame,1)

        cv2.putText(frame, datetime.now().strftime('%d/%m/%y %H:%M:%S'), (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,255))
        cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        vidimg = Image.fromarray(cv2img)

        imgtk = ImageTk.PhotoImage(image=vidimg)
        lab1.configure(image=imgtk)
        lab1.imgtk = imgtk
        lab1.after(10, showfeed)
    else:
        lab1.configure(image="")
#===========================================================================

#Finding Save Folder========================================================
def desbrowse():
    desDir = filedialog.askdirectory(initialdir="Your Directory Path")
    desPath.set(desDir)
#==========================================================================

#Capture Image And Then Save===============================================
def capture():
    global lab3
    imgname = datetime.now().strftime('%d-%m-%y %H-%M-%S')
    if desPath.get()!="":
        imgPath = desPath.get()

    else:
        messagebox.showerror("Error", "Select A Path Directory")

    imgname = imgPath+'/'+imgname+".jpg"

    ret, frame = root.cap.read()
    cv2.putText(frame, datetime.now().strftime('%d/%m/%y %H:%M:%S'), (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5,(0, 255, 255))
    noice = cv2.imwrite(imgname, frame)
    save = Image.open(imgname)
    save = ImageTk.PhotoImage(save)

    lab3.config(image=save)
    lab3.photo = save

    if noice:
        messagebox.showinfo("Noice One", "Image Saved at"+ imgname)
#=====================================================================================================

#Stop and Start Camera Video=====================================
def stop():
    global btn2
    root.cap.release()

    btn2.config(text="Open Cam", command=start)
    lab1.config(text="Close Cam", font=20)
def start():
    global btn2
    root.cap = cv2.VideoCapture(0)
    width1,height1 = 640,480
    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width1)
    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height1)

    btn2.config(text="Close Cam", command=start)
    lab1.config(text="")
    showfeed()
#=============================================================


root = tk.Tk()
root.cap = cv2.VideoCapture(0)
# width, height = 640, 480
# root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# root.title("Interface")
# root.geometry("1300x1300")
# root.configure(background="steelblue")

desPath = StringVar()
imgPath = StringVar()

#widgets()
#root.mainloop()
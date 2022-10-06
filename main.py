import tkinter as tk
from tkinter import *
import os

def kill():
    screen1.destroy()

def function1():
    screen3.destroy()

def saved():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Note")
    screen6.geometry("100x100")
    Label(screen6, text = "saved").pack()


def save():

    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()

def create():
    global raw_filename
    global raw_notes
    raw_filename = StringVar()
    raw_notes = StringVar()

    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Note")
    screen5.geometry("800x800")
    Label(screen5, text="File Name").pack()
    Entry(screen5, textvariable=raw_filename).pack()
    Label(screen5, text="Create Note").pack()
    Entry(screen5, textvariable=raw_notes).pack()
    Button(screen5, text = "Save", command = save).pack()

def view_notes():
    global screen7
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen7 = Toplevel(screen)
    screen7.title("Note")
    screen7.geometry("800x800")
    Label(screen7, text=data1).pack()



def view():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Note")
    screen7.geometry("800x800")

    all_files = 'Attend.csv'
    Label(screen7, text="Files").pack()
    Label(screen7, text=all_files).pack()
    #
    # global raw_filename1
    # raw_filename1 = StringVar()
    # Entry(screen7, textvariable=raw_filename1).pack()
    Button(screen7, command=view_notes, text = "OK").pack()

def delete_note1():
    global screen9
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen9 = Toplevel(screen)
    screen9.title("Note")
    screen9.geometry("800x800")
    Label(screen9, text=filename3+" removed").pack()



def delete():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Note")
    screen8.geometry("800x800")
    all_files = os.listdir()
    Label(screen8, text="Files").pack()
    Label(screen8, text=all_files).pack()

    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen8, textvariable=raw_filename2).pack()
    Button(screen8, command=delete_note1, text="OK").pack()


def session():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("dashboard")
    screen4.geometry("800x485")

    Label(screen4,text = "Welcome User").pack()
    Label(screen4,text="").pack()
    Button(screen4, text="Create Note", height=10, width=40, command=create).pack()
    Label(screen4,text="").pack()
    Button(screen4, text="View Note", height=10, width=40, command=view).pack()
    Label(screen4,text="").pack()
    Button(screen4, text="Delete Note", height=10, width=40, command=delete).pack()
    Label(screen4,text="").pack()

def login_sucess():
    session()

def password_not_verified():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Log")
    screen3.geometry("150x100")
    Label(screen3, text="Password Incorrect").pack()
    Button(screen3, text="OK", command=function1).pack()

def user_not_found():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Log")
    screen3.geometry("150x100")
    Label(screen3, text="User Not Registered").pack()
    Button(screen3, text="OK", command=function1).pack()

def register_user():

    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Is Succesful", fg = "green", font = ("Calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_verified()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Enter Information Below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x400")
    Label(screen2, text="Enter Information Below").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login", width=10, height=1, command=login_verify).pack()


def mainscreen():
    global screen
    screen = Tk()
    screen.geometry("400x400")
    screen.title("HW Interface 1.0")
    Label(screen, text = "HW Interface 1.0", bg="lightblue", height = "2", width = "300", font = ("Calibri", 13)).pack()

    Label(text="").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()



    screen.mainloop()

mainscreen()

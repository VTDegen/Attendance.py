from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Interface')
root.iconbitmap('Logo.ico')
root.geometry("500x500")

img = Image.open("ImagesBasic/JuliusTest.jpg")

res = img.resize((300,300), Image.ANTIALIAS)

img = ImageTk.PhotoImage(res)

l1 = Label(root, image=img).pack()
b1 = Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
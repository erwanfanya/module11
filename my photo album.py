from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("My photo album")
root.geometry("400x420")

title = Label(root, text=' My photo album', fg='White', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('dogjpeg.jpeg')
img_file = img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(root, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo(' Great!', 'you clicked the photo!')
msg_btn = Button(root, text='Click me to React', bg= 'blue', fg='white', command = show_message)
msg_btn.pack(pady=5)

def show_details():
    top = Toplevel()
    top.title('Photo details')
    top.geometry('200x120')
    info = Label(top, text= ' Taken on : June first 2025')
    info.pack(pady=10)
    place = Label(top, text= ' Location : my garden in new york city')
    place.pack()
    top.mainloop()
details_btn = Button(root, text = ' See details', bg='green', fg='white', command= show_details)
details_btn.pack(pady=5)

root.mainloop()
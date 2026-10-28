from tkinter import *

root = Tk()
root.title("My profile card")
root.geometry("400x380")

title= Label(root, text="My profile card", fg='white', bg = 'purple', width= 40)
title.grid(row=0, column=0, columnspan= 2, padx=10, pady=10)

name_label = Label(root,text="Name:", fg = 'black', bg='white')
name_label.grid(row=1, column=0, padx= 10, pady=10)

name_entry= Entry(root, fg='white', bg='light yellow', width='25')
name_entry.grid(row=1, column=1, padx=10, pady=10)

hobby_label = Label(root, text= "Hobby:", fg = "black", bg="white")
hobby_label.grid(row= 2, column= 0, padx= 10, pady=10)

hobby_entry = Entry(root, fg= "blue", bg="light yellow", width= "25")
hobby_entry.grid(row= 2, column= 1, padx=10, pady=10)

about_frame = Frame(root, relief=RAISED, borderwidth = 3)
about_frame.grid(row=3, column=0, columnspan= 2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me:")
about_label.pack()
about_text = Text(about_frame, fg= "green", bg="light yellow", width= 40, height= 4)
about_text.pack()

submit = Button(root, text="Show my card", bg="purple", fg="white", width=20)
submit.grid(row=4, column=0, columnspan= 2, padx=10, pady=10)

root.mainloop()




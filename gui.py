from tkinter import *

root = Tk()

root.title("I see you")
root.geometry("200x75")

app = Frame(root)
app.grid()
label = Label(app, text = "This software is for you! Do you like it")
label.grid()

button1 = Button(app, text = "Yes")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text ="No")

root.mainloop()


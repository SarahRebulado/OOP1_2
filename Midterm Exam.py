# import tkinter module
from tkinter import *

# create a tkinter window
window = Tk()

# Title to the window
window.title("Special Midterm Exam in OOP")

# Title size
window.geometry("500x400+20+10")


# Create a button and assign color
def change_color():
    btn.configure(bg="Yellow")


btn = Button(window, text="Click to Change Color", command=change_color)
btn.place(relx=.5, y=200,
          anchor="center")

# Initialize the window
window.mainloop()

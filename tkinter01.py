from tkinter import *

window = Tk()  # Making instance of window
window.geometry("420x420")
window.title("Etykieciarz")

icon = PhotoImage(file="grafika/logo.png")
window.iconphoto(True, icon)
window.config(background="#c8c7d1")

window.mainloop()  # Place window on computer screen

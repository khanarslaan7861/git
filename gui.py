from tkinter import *


window = Tk()
window.title("Not the title")
window.geometry("1366x768")
window.minsize(1366, 768)
window.maxsize(1366, 768)
Label(window, text="Dare not look here", bg="red", fg="black").place(x=100, y=200)
Label(window, text="You looked here", bg="yellow", fg="black").place(x=100, y=220)
Label(window, text="NOO you looked there too", bg="pink", fg="black").place(x=100, y=240)
window.mainloop()

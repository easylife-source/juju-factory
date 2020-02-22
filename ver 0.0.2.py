from tkinter import *
window = Tk()

buttons = []

def position(pos):
    print(pos)

def OnButtonClick(btnid):
    print(btnid)

for i in range(10):
    for n in range(16):
        buttons.append(Button(window, width = 5, height = 2, bg = "red", command = lambda: OnButtonClick(n*i)).grid(row = n, column = i))


window.mainloop()

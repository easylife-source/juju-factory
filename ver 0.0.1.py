from tkinter import *
window = Tk()

buttons = []

def position(pos):
    print(pos)

def OnButtonClick(self, button_id):
    if button_id == 1:
        print("1111")
    elif button_id == 2:
        print("22222")

for i in range(10):
    for n in range(16):
        buttons.append(Button(window, width = 5, height = 2, bg = "red", command = lambda: OnButtonClick(2)).grid(row = n, column = i))


window.mainloop()

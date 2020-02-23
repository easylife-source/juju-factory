from tkinter import*
master=Tk()
master.title('Testing')
button = []
for n in range(16):
    for l in range(10):
        button.append(Button(master,width=2,bg = 'red', command = lambda: OnButtonClick(self,1234)))
        button[l].grid(row=n,column=l)

master.mainloop()

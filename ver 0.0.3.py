from tkinter import*
master=Tk()
master.title('Testing')
button = []
fid=[1,3,5,7,9,11,13,15,17,19]
sid=[0,2,4,6,8,10,12,14,16,18,20]
f = 0
isodd = True
def OnButtonClick(bid):
   button[bid].configure(bg="blue")
for n in range(10):
    for l in range(16):
        button.append(Button(master,width=4,height=2, bg = 'red',text = f, command = lambda: button[f].text))
        if isodd == True:
            button[f].grid(row=l, column=fid[n])
            print(fid[n])
            f=f+1
        elif isodd == False:
            button[f].grid(row = l, column = sid[n])
            f = f+1
    if isodd == True:
        isodd=False
    else:
        isodd=True
    print(isodd)

master.mainloop()

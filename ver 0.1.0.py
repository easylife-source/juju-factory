from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import webbrowser
import os
root = Tk()

files = [] #creates list to replace your actual inputs for troubleshooting purposes
btn = []
color=[]
colorlist = ["red","blue","green","pink","yellow","orange","white","purple","black","grey"]
allcolor=len(colorlist)
#creates list to store the buttons ins
i1 = -1
root.title('JUJU Builder (Version 0.1.1)')
for i in range(189): #this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
    files.append(str(i))
row = 0
odd = 0
def ChangeColor(button):
    if color[int(button)] >= allcolor-1:
         color[int(button)]=-1
         btn[int(button)].configure(bg=colorlist[color[int(button)]+1])
    else:
        btn[int(button)].configure(bg=colorlist[color[int(button)]+1])
        color[int(button)]=color[int(button)]+1
# Update#

def checkupdate():
  #updatercode
  #updatercode
  #updatercode is not open source
  print('updater code is not open source, please cosider using our Official Release.')
  messagebox.showinfo("Code is not open", 'Updater code is not open source, please cosider using our Official Release.')
odd = 0
checkupdate()   
for i in range(len(files)): #this says for *counter* in *however many elements there are in the list files*
    #the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
    if odd == 0:
        i1 = i1+1
        btn.append(Button(root,width=4,height=2, text=files[i], command=lambda c=i:(ChangeColor(btn[c].cget("text")))))
        color.append(-1)
        if i1 == 10:
            i1 = 0
            row = row+1
            odd = 1
        else:
            btn[i].grid(row=row,column=i1+1)
    elif odd == 1:
        btn.append(Button(root,width=4,height=2, text=files[i], command=lambda c=i:(ChangeColor(btn[c].cget("text")))))
        color.append(-1)
        if i1 == 10:
            row = row+1
            i1 = i1-1
            odd = 0
        else:
            btn[i].grid(row=row,column=i1+1)
            i1 = i1+1
        #btn[i].pack() #this packs the buttons

root.mainloop()

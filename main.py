from tkinter import *
import os

from login import Root



def moc(n):
    if n==1:

        root.withdraw()

        Root(root)

    else:
        root.mainloop()



root=Tk()
root.title ("BMS")
root.resizable(False, False)
mainIc=PhotoImage(file="ecorp.png")
mainIcon=PhotoImage(file="user.png")
mainIcon2=PhotoImage(file="group-profile-users.png")
root.iconphoto(False,mainIc)
root.geometry("768x600")

Label(root,text="E-Corp Billing System",font=('Verdana',28)).pack(side=TOP,pady=30)
mainIcon=mainIcon.subsample(2,2)
mainIcon2=mainIcon2.subsample(2,2)

bt1=Button(root,text="ADMIN",image=mainIcon,compound=TOP,command=moc(1))
bt1.place(x=80,y=150)
bt2=Button(root,text="USER",image=mainIcon2,compound=TOP,command=moc(2))
bt2.place(x=400,y=150)

root.resizable(False,False)
root.mainloop()


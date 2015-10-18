# -*- coding: utf-8 -*-
# write python3.5
from tkinter import *

class test(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.exit = Button(self,text="네 공부할게요 ㅠㅠ",bg="gray",padx=0,pady=0,fg="black")
        self.exit.bind("<Button-1>", self.exit_chk)            
        self.exit.place(x=100,y=100)

    def exit_chk(self, event):
        self.destroy()


root = test(None)
root.title('하라는 공부는 안하고!')
root.geometry("340x240+0+0")
root.mainloop()
              

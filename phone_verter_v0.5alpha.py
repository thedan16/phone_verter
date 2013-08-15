#-------------------------------------------------------------------------------
# Name:        Application
# Purpose:
#
# Author:      Daniel Beall
#
# Created:     14/08/2013
# Copyright:   None! :)
# Licence:     MIT
#-------------------------------------------------------------------------------

from Tkinter import *
class Application(Frame):



    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "PhoneConverter")
        self.instruction.grid(row = 0,  column =0, columnspan = 2, sticky = W)

        self.phonenumberletters = Entry(self)
        self.phonenumberletters.grid(row = 1, column = 1, sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row =2, column = 0, sticky =W)



        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan =2, sticky = W)



    def reveal(self):
        phonestring = self.phonenumberletters.get().lower()
        c = 0
        digitstring = ""
        for z in range(0, len(phonestring)):
            if phonestring[z].isdigit() == True:
                c = c + 1
                digitstring = digitstring + phonestring[z]




        phone = {"a": "2", "b": "2", "c": "2", "d": "3", "e": "3", "f" : "3", "g": "4", "h": "4", "i": "4",
        "j": "5", "k": "5", "l": "5", "m": "6", "n": "6", "o": "6", "p": "7", "q": "7","r": "7", "s": "7", "t": "8", "u": "8", "v": "8", "w": "9", "x": "9", "y": "9", "z": "9"}

        finalstring =  ""


        for i in range(c, len(phonestring)):

            finalstring = finalstring + phone[phonestring[i]]

        finalstring = digitstring + finalstring

        self.text.insert(0.0, finalstring)

root = Tk()
root.title("PhoneLetters")
root.geometry("250x150")
app = Application(root)

root.mainloop()

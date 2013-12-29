#-------------------------------------------------------------------------------
# Name:        Application
# Purpose:
#
# Author:      Daniel Beall
#
# Created:     7/12/2013
# Copyright:   None! :)
# Licence:     MIT
#-------------------------------------------------------------------------------

from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import itertools
import signal
class Application(Frame):

    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        self.topbar()

#open a txt file
    def filesystem_access(self):
        try:
            filename = open(askopenfilename(filetypes=[("allfiles","*"),("textfiles","*.txt")]))
            fetchedstring = filename.read()
            self.outputfromfile(fetchedstring)
        except:
            pass
#save to a text file
    def savetofilesystem(self):
        result = tkMessageBox.askquestion("Choose Texbox to save", "Save the Left Textbox?")
        if result == 'yes':    
            filename = open(askopenfilename(filetypes=[("textfiles - will overwrite","*.txt")]),"w")
            filename.write(self.text.get(0.0,END))
        else:
            result = tkMessageBox.askquestion("Choose Texbox to save", "Save the Right Textbox?")
            if result == 'yes':
                filename = open(askopenfilename(filetypes=[("textfiles - will overwrite","*.txt")]),"w")
                filename.write(self.textbox2.get(0.0,END))
            else:
                pass

    def create_widgets(self):
        #left boxes
        self.instruction = Label(self, text = "Letters to Numbers")
        self.instruction.grid(row = 0,  column =0, columnspan = 1, sticky = W)

        self.phonenumberletters = Entry(self)
        self.phonenumberletters.grid(row = 1, column = 0, sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row =1, column = 1 , sticky =W)

        self.delete_button = Button(self, text = "Clear", command = self.delete)
        self.delete_button.grid(row =2, column = 1, sticky =W)

        self.text = Text(self, width = 35, height = 15, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan =2, sticky = W)

        self.checkboxstate = BooleanVar()
        self.checkbox = Checkbutton(self, text = "Output number on new line", variable = self.checkboxstate)
        self.checkbox.grid(row =2, column = 0, sticky = W)

        #second pair of boxes
        self.instruction2 = Label(self, text = "Numbers to Letters")
        self.instruction2.grid(row = 0, column = 7, columnspan = 1, sticky = W)
		
        self.textbox2 = Text(self, width = 35, height = 15, wrap = WORD)
        self.textbox2.grid(row = 3, column = 7, columnspan =2 , sticky = W)
        
        self.submit_button2 = Button(self, text = "Submit", command = self.convert_to_options)
        self.submit_button2.grid(row = 1, column = 9, sticky = W)

        self.delete_button2 = Button(self, text = "Clear", command = self.delete2)
        self.delete_button2.grid(row = 2, column = 9, sticky = W) 
        
        self.phonenumber_to_words = Entry(self)
        self.phonenumber_to_words.grid(row = 1, column = 8, sticky = W)
		
        


# makes Menu Bars
    def topbar(self):
        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open - only converts from Letters to Numbers", command=self.filesystem_access)
        filemenu.add_command(label="Save", command=self.savetofilesystem)

        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=helpmenu)


        root.config(menu=menubar)

# displays About my app
    def hello(self):
        tkMessageBox.showinfo("Help - Phone Verter <2013>", "Version 2.0 \n Licensed Under the MIT license \n Built and maintained by Daniel Beall \n Contact: thedan16@users.sourceforge.net  ")

#output when button is pressed
    def reveal(self):
        #take input from text box
        phonestring = self.phonenumberletters.get().lower()
        phone = {"a": "2", "b": "2", "c": "2", "d": "3", "e": "3", "f" : "3", "g": "4", "h": "4", "i": "4",
        "j": "5", "k": "5", "l": "5", "m": "6", "n": "6", "o": "6", "p": "7", "q": "7","r": "7", "s": "7", "t": "8", "u": "8", "v": "8", "w": "9", "x": "9", "y": "9", "z": "9"}
        finalstring = ""
        for z in range(0, len(phonestring)):
            if phone.has_key(phonestring[z]):
                finalstring = finalstring + phone[phonestring[z]]
            else:
                finalstring = finalstring + phonestring[z]

        if self.checkboxstate.get():
            self.text.insert(0.0, "\n" + finalstring)
        else:
            self.text.insert(0.0, " " + finalstring)

    #output from a text file
    def outputfromfile(self, fileinput):
        phonestring = fileinput.lower()
        phone = {"a": "2", "b": "2", "c": "2", "d": "3", "e": "3", "f" : "3", "g": "4", "h": "4", "i": "4",
        "j": "5", "k": "5", "l": "5", "m": "6", "n": "6", "o": "6", "p": "7", "q": "7","r": "7", "s": "7", "t": "8", "u": "8", "v": "8", "w": "9", "x": "9", "y": "9", "z": "9"}
        finalstring = ""
        for z in range(0, len(phonestring)):
            if phone.has_key(phonestring[z]):
                finalstring = finalstring + phone[phonestring[z]]
            else:
                finalstring = finalstring + phonestring[z]

        self.text.insert(0.0, finalstring)
		
    #converts phonenumber to all possible letter combos	
    def convert_to_options(self):
            z = self.phonenumber_to_words.get()
            set1 = ["1"]
            set2 = ["a","b","c"]
            set3 = ["d","e","f"]
            set4 = ["g","h","i"]
            set5 = ["j","k","l"]
            set6 = ["m","n","o"]
            set7 = ["p","q","r","s"]
            set8 = ["t","u","v"]
            set9 = ["w","x","y","z"]

            tup1 = ();

            for x in range(0,len(z)):

                    try:
                            c = int(z[x])
                    except:
                            tup1 = tup1 + ([z[x]],)
                            c=-1
                            
                    if c == 0:
                    	tup1 = tup1 + ("0",)
                    
                    if c == 1:
                            tup1 = tup1 + (set1,)
                            
                    if c == 2:
                            tup1 = tup1 + (set2,)

                    if c == 3:
                            tup1 = tup1+ (set3,)

                    if c == 4:
                            tup1 = tup1+ (set4,)

                    if c == 5:
                            tup1 = tup1+ (set5,)

                    if c == 6:
                            tup1 = tup1+ (set6,)

                    if c == 7:
                            tup1 = tup1+ (set7,)

                    if c == 8:
                            tup1 = tup1+ (set8,)

                    if c == 9:
                            tup1 = tup1+ (set9,)
                            
            
            if len(tup1) < 15:
                for i in itertools.product(*tup1):
                        output = ""
                        for z in xrange(0,len(i)):
                                output = output + str(i[z])

                        self.textbox2.insert(0.0, "\n" + output)
            else:
                self.textbox2.insert(0.0, "\n" + str(tup1))
                self.textbox2.insert(0.0, "Error: Reduce size of phone number. Use dashes to separate number sequences") 
                    
            self.textbox2.insert(0.0, "\n" + "------------------------")
			
				


    #clear Text Area
    def delete(self):
        self.text.delete(0.0, END)

    def delete2(self):
        self.textbox2.delete(0.0, END)



root = Tk()
root.title("PhoneVerter 2.0")
root.geometry("750x400")
app = Application(root)

root.mainloop()

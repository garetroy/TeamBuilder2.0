'''
@author Garett Roberts
created: Thurs Apr 27 3:00:00 PDT 2017

This creates a gui for the Team Builder.

'''
from tkinter import Tk, Frame, RIGHT, BOTH, RAISED, TOP, X, N, LEFT, messagebox, Toplevel, Toplevel, DISABLED,ACTIVE
from tkinter.ttk import Style, Button, Label, Entry
from subprocess import call
import os

class Root(Frame):
    '''
    The root window
    '''

    def __init__(self,parent): 
        '''
            Initilization of the window, assigning height
            centering the window, and starting the interface.
        '''
        Frame.__init__(self, parent, background="white")

        self.h = 290 
        self.w = 600
        self.parent = parent
        self.parent.title("Input screen")
        self.pack(fill=BOTH, expand=1)

        self.centerWindow()
        self.startUI()

    def centerWindow(self):
        '''
        This centers the window into place
        '''
    
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - self.w) / 2
        y = (sh - self.h) / 2

        self.parent.geometry('%dx%d+%d+%d' % (self.w,self.h, x ,y))

    def startUI(self):
        '''
        Starting the UI takes some work, this creates the buttons
        labels and entrys. Also puts them into place, and adds
        function calls to the buttons
        '''

        self.style = Style()         
        self.style.theme_use("default")

        csvFrame = Frame(self)
        csvFrame.pack(fill=X, side=TOP)

        csvLabel = Label(csvFrame, text="Path to csv:", background="white")
        csvLabel.pack(side=LEFT, padx=15, pady=30)

        self.csvEntry = Entry(csvFrame) 
        self.csvEntry.pack(side=LEFT, padx=37, pady=30)

        csvButton = Button(csvFrame, command=self.startfilebrowser, text="Browse...") 
        csvButton.pack(side=LEFT, padx=0, pady=30)

        roosterFrame = Frame(self)
        roosterFrame.pack(fill=X, side=TOP)

        roosterLabel = Label(roosterFrame, text="Path to rooster:", background="white")
        roosterLabel.pack(side=LEFT, padx=15, pady=30)

        self.roosterEntry = Entry(roosterFrame) 
        self.roosterEntry.pack(side=LEFT, padx=15, pady=30)

        roosterButton = Button(roosterFrame, command=self.startfilebrowser, text="Browse...") 
        roosterButton.pack(side=LEFT, padx=18, pady=30)

        outputFrame= Frame(self)
        outputFrame.pack(fill=X, side=TOP)

        outputLabel = Label(outputFrame, text="Team size:", background="white")
        outputLabel.pack(side=LEFT, padx=15, pady=30)

        self.outputEntry = Entry(outputFrame, width=5) 
        self.outputEntry.pack(side=LEFT, padx=15, pady=20)

        frame = Frame(self, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        exitButton = Button(self,text="Exit",command=self.parent.destroy)
        exitButton.pack(side=RIGHT, padx=5, pady=5)
        self.submitButton = Button(self,text="Submit",command=self.submitFiles)
        self.submitButton.pack(side=RIGHT)


    def submitFiles(self):
        '''
        Checks the validity of the entry feilds for
        correct paths and a proper team size.
        After checks it runs our python script.
        '''
        csvtext     = self.csvEntry.get()
        teamsize    = self.outputEntry.get()
        roostertext = self.roosterEntry.get()

        if(not os.path.exists(csvtext) and csvtext[-4:] != ".csv"):
            messagebox.showinfo("Error","Not a CSV or the file does not exist")
            return

        if(not os.path.exists(roostertext) and roostertext[-4:] != ".txt"): 
           messagebox.showinfo("Error","Not a rooster or the file does not exist")
           return

        if not self.testNumber(teamsize):
            messagebox.showinfo("Error","Please enter a positive integer for teamsize") 

        outpath = "~/Desktop/out.txt" #needs changing... Might show on own display
        call(["python3","../TeamBuilder/src/team_builder.py",csvtext,roostertext,outpath,teamsize])


    def testNumber(self,i):
        '''
        Checks if i is an integer and between
        a certain range
        
        @param:
            i (string) 
        '''
        try:
            i = int(i)
            return (i > 0) and (i < 5) #can change teamsize max here
        except:
            return False

    def startfilebrowser(self):
        pass

if __name__ == "__main__": 
    root = Tk()
    ex = Root(root)
    root.mainloop()


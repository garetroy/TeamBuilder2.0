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

        #CREATING CSV FRAME
        csvFrame = Frame(self)
        csvFrame.pack(fill=X, side=TOP)

        csvLabel = Label(csvFrame, text="Path to csv:", background="white")
        csvLabel.pack(side=LEFT, padx=15, pady=30)

        self.csvEntry = Entry(csvFrame) 
        self.csvEntry.pack(side=LEFT, padx=37, pady=30)

        csvButton = Button(csvFrame, command=self.startfilebrowser, text="Browse...") 
        csvButton.pack(side=LEFT, padx=0, pady=30)
        #DONE CSV FRAME

        #CREATING ROSTER FRAME
        rosterFrame = Frame(self)
        rosterFrame.pack(fill=X, side=TOP)

        rosterLabel = Label(rosterFrame, text="Path to roster:", background="white")
        rosterLabel.pack(side=LEFT, padx=15, pady=30)

        self.rosterEntry = Entry(rosterFrame) 
        self.rosterEntry.pack(side=LEFT, padx=15, pady=30)

        rosterButton = Button(rosterFrame, command=self.startfilebrowser, text="Browse...") 
        rosterButton.pack(side=LEFT, padx=18, pady=30)
        #DONE ROSTER FRAME

        #CREATING TEAMSIZE FRAME
        teamsizeFrame= Frame(self)
        teamsizeFrame.pack(fill=X, side=TOP)

        outputLabel = Label(teamsizeFrame, text="Team size:", background="white")
        outputLabel.pack(side=LEFT, padx=15, pady=30)

        self.outputEntry = Entry(teamsizeFrame, width=5) 
        self.outputEntry.pack(side=LEFT, padx=15, pady=20)
        #DONE TEAMSIZE FRAME

        #CREATING BOTTOM BUTTONS
        frame = Frame(self, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        exitButton = Button(self,text="Exit",command=self.parent.destroy)
        exitButton.pack(side=RIGHT, padx=5, pady=5)
        self.submitButton = Button(self,text="Submit",command=self.submitFiles)
        self.submitButton.pack(side=RIGHT)
        #DONE BOTTOM BUTTONS


    def submitFiles(self):
        '''
        Checks the validity of the entry feilds for
        correct paths and a proper team size.
        After checks it runs our python script.
        '''
        csvtext     = self.csvEntry.get()
        teamsize    = self.outputEntry.get()
        rostertext = self.rosterEntry.get()

        #Checking existance of paths and extensions
        if(not os.path.exists(csvtext) and csvtext[-4:] != ".csv"):
            messagebox.showinfo("Error","Not a CSV or the file does not exist")
            return

        if(not os.path.exists(rostertext) and rostertext[-4:] != ".txt"): 
           messagebox.showinfo("Error","Not a roster or the file does not exist")
           return

        #Checking if the string is an int and in range
        if not self.testNumber(teamsize):
            messagebox.showinfo("Error","Please enter a positive integer for teamsize") 

        outpath = "~/Desktop/out.txt" #needs changing... Might show on own display
        call(["python3","../TeamBuilder/src/team_builder.py",csvtext,rostertext,outpath,teamsize])


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


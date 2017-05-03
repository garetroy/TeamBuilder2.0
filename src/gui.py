'''
@author Garett Roberts
created: Thurs Apr 27 3:00:00 PDT 2017

This creates a gui for the Team Builder.

modified: Garett Roberts Thurs Apr 29 2:40 PDT 2017
Added file browser and output directory

'''
from tkinter import Tk, Frame, RIGHT, BOTH, RAISED
from tkinter import TOP, X, N, LEFT, messagebox
from tkinter import Toplevel, Toplevel, DISABLED
from tkinter import ACTIVE, filedialog
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
        csvLabel.pack(side=LEFT, padx=15, pady=10)

        self.csvEntry = Entry(csvFrame) 
        self.csvEntry.pack(side=LEFT, padx=35, pady=10)

        csvButton = Button(csvFrame, command=self.csvstartfilebrowser, text="Browse...") 
        csvButton.pack(side=LEFT, padx=10, pady=10)
        #DONE CSV FRAME

        #CREATING ROSTER FRAME
        rosterFrame = Frame(self)
        rosterFrame.pack(fill=X, side=TOP)

        rosterLabel = Label(rosterFrame, text="Path to roster:", background="white")
        rosterLabel.pack(side=LEFT, padx=17, pady=10)

        self.rosterEntry = Entry(rosterFrame) 
        self.rosterEntry.pack(side=LEFT, padx=15, pady=10)

        rosterButton = Button(rosterFrame, command=self.rosterstartfilebrowser, text="Browse...") 
        rosterButton.pack(side=LEFT, padx=28, pady=10)
        #DONE ROSTER FRAME

        #CREATING OUTPUT FRAME
        outputFrame = Frame(self)
        outputFrame.pack(fill=X, side=TOP)

        outputLabel = Label(outputFrame, text="Path to output:", background="white")
        outputLabel.pack(side=LEFT, padx=15, pady=10)

        self.outputEntry = Entry(outputFrame) 
        self.outputEntry.pack(side=LEFT, padx=15, pady=10)

        outputButton = Button(outputFrame, command=self.outputstartfilebrowser, text="Browse...") 
        outputButton.pack(side=LEFT, padx=28, pady=10)
        #DONE OUTPUT FRAME

        #CREATING TEAMSIZE FRAME
        teamsizeFrame= Frame(self)
        teamsizeFrame.pack(fill=X, side=TOP)

        teamsizeLabel = Label(teamsizeFrame, text="Team size:", background="white")
        teamsizeLabel.pack(side=LEFT, padx=15, pady=10)

        self.teamsizeEntry = Entry(teamsizeFrame, width=5) 
        self.teamsizeEntry.pack(side=LEFT, padx=43, pady=10)
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
        teamsize    = self.teamsizeEntry.get()
        rostertext  = self.rosterEntry.get()
        outputtext  = self.outputEntry.get()
        currpath    = os.getcwd() + "/team_builder.py" #may need changing

        #Checking existance of path
        if(not os.path.exists(currpath)):
           messagebox.showinfo("Error","Cannot find team_builder.py!")
           self.parent.destroy()
           return

        #Checking existance of paths and extensions
        if(not os.path.exists(csvtext) and csvtext[-4:] != ".csv"):
            messagebox.showinfo("Error","Not a CSV or the file does not exist")
            return

        #Checking existance of paths and extensions
        if(not os.path.exists(rostertext) and rostertext[-4:] != ".txt"): 
           messagebox.showinfo("Error","Not a roster or the file does not exist")
           return

        #Checking existance of path
        if(not os.path.exists(outputtext)):
           messagebox.showinfo("Error","Directory dosen't exists for output")
           return

        #Checking if the string is an int and in range
        if(not self.testNumber(teamsize)):
            messagebox.showinfo("Error","Please enter a positive integer for teamsize") 
            return

        outputtext += "/out.txt"
        call(["python3","team_builder.py",csvtext,rostertext,outputtext,teamsize])


    def testNumber(self,i,minimum=0,maximum=5):
        '''
        Checks if i is an integer and between
        a certain range
        
        @param:
            i (string) 
            minimum (optional int)
            maximum (optional int)
        '''
        try:
            i = int(i)
            return (i >= minimum) and (i <= maximum) 
        except:
            return False

    def csvstartfilebrowser(self):
        '''
        Starts the filebrowser for the csv file
        '''
        currdir = os.getcwd()
        fileopt = [('csv files', '*.csv')]
        directo = filedialog.askopenfilename(parent=self, filetypes=fileopt, \
                                         initialdir=currdir, title="Select file")
        #clearning and setting csventry
        self.csvEntry.delete(0,'end')
        self.csvEntry.insert(0,str(directo))

    def rosterstartfilebrowser(self):
        '''
        Starts the filebrowser for the text file
        '''
        currdir = os.getcwd()
        fileopt = [('text files', '*.txt')]
        directo = filedialog.askopenfilename(parent=self, filetypes=fileopt, \
                                         initialdir=currdir, title="Select file")
        #clearning and setting rosterentry 
        self.rosterEntry.delete(0,'end')
        self.rosterEntry.insert(0,str(directo))
        
    def outputstartfilebrowser(self):
        '''
        Starts the filebrowser for the output 
        '''
        currdir = os.getcwd()
        directo = filedialog.askdirectory(parent=self,\
                                    initialdir=currdir, title="Select file")

        #clearning and setting outputentry 
        self.outputEntry.delete(0,'end')
        self.outputEntry.insert(0,str(directo))
        

if __name__ == "__main__": 
    root = Tk()
    root.resizable(width=False, height=False)
    ex = Root(root)
    root.mainloop()

'''
@author Garett Roberts
created: Thurs Apr 27 3:00:00 PDT 2017

This creates a gui for the Team Builder.

modified: Garett Roberts Thurs Apr 29 14:40 PDT 2017
Added file browser and output directory

modified: Garett Roberts Sat May 6 10:00 PDT 2017
Added option screen

modified: Garett Roberts Sat May 7 5:36 PDT 2017
Saves input screen's entries now

modified: Garett Roberts Sun May 8 6:00 PDT 2017
Added loading screen and multithreading events

modified: Howard Lin Wed May 11 4:00 PDT 2017
Added a member swap screen

modified: Alister Maguire Sun May 14 19:04:13 PDT 2017
Added optional command line arguments for csv and roster
paths. 

'''
import os
import time
import threading
import argparse
from tkinter         import Tk, Frame, RIGHT, BOTH, RAISED
from tkinter         import TOP, X, N, LEFT, messagebox
from tkinter         import END, Listbox, MULTIPLE
from tkinter         import Toplevel, DISABLED
from tkinter         import ACTIVE, filedialog, NORMAL
from tkinter.ttk     import Style, Button, Label, Entry
from tkinter.ttk     import Progressbar, Checkbutton
from guiinterface    import GuiInterface
from multiprocessing import Queue

class Root(Frame):
    '''
    The root window
    '''
    def __init__(self,parent,csvpath="",rosterpath=""):
        '''
        Initilization of the window, assigning height
        centering the window, and starting the interface.
        '''
        self.queue       = Queue()
        self.parent      = parent
        self.interface   = GuiInterface()
        self.loadWindow  = None
        self.remember    = False
        self.initialized = False
        self.csvpathh    = csvpath
        self.rosterpathh = rosterpath
        self.outpathh    = ""
        self.teamsizeh   = ""

        self.startMainUI()

    def centerWindow(self,notself=None):
        '''
        This centers the window into place
        if notself is set, then it centers
        the notself window

        @param:
            notself - TKobject
        '''

        if notself != None: #notself is primarly for progressbar
            sw = self.parent.winfo_screenwidth()
            sh = self.parent.winfo_screenheight()
            x = (sw - self.w/2) / 2
            y = (sh - self.h/2) / 2
            notself.geometry('%dx%d+%d+%d' % (self.w/1.8,self.h/1.8, x,y))
        else:
            sw = self.parent.winfo_screenwidth()
            sh = self.parent.winfo_screenheight()
            x = (sw - self.w) / 2
            y = (sh - self.h) / 2
            self.parent.geometry('%dx%d+%d+%d' % (self.w,self.h, x ,y))

    def startWindow(self):
        '''
        This method starts/creates the window for
        the UI
        '''
        Frame.__init__(self, self.parent, background="white")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        if(not self.initialized):
            self.centerWindow()
        else:
            self.parent.geometry('%dx%d' % (self.w,self.h))
        self.initialized = True

    def resetWindow(self):
        '''
        Resets the window
        '''
        if(self.initialized):
            self.destroy()
        if(self.loadWindow != None):
            self.loadWindow.destroy()

        self.startWindow()

    def startMainUI(self):
        '''
        Starting the main UI takes some work, this creates the buttons
        labels and entrys. Also puts them into place, and adds
        function calls to the buttons
        '''
        #RESETING WINDOW
        self.h           = 290
        self.w           = 600
        self.resetWindow()
        self.parent.title("Input")

        #CREATING CSV FRAME
        csvFrame = Frame(self)
        csvFrame.pack(fill=X, side=TOP)

        csvLabel = Label(csvFrame, text="Path to csv:", background="white")
        csvLabel.pack(side=LEFT, padx=15, pady=10)

        self.csvEntry = Entry(csvFrame, width=30)
        self.csvEntry.insert(0,self.csvpathh)
        self.csvEntry.pack(side=LEFT, padx=35, pady=10)

        csvButton = Button(csvFrame, command=self.csvstartfilebrowser, text="Browse...")
        csvButton.pack(side=LEFT, padx=10, pady=10)
        #DONE CSV FRAME

        #CREATING ROSTER FRAME
        rosterFrame = Frame(self)
        rosterFrame.pack(fill=X, side=TOP)

        rosterLabel = Label(rosterFrame, text="Path to roster:", background="white")
        rosterLabel.pack(side=LEFT, padx=17, pady=10)

        self.rosterEntry = Entry(rosterFrame, width=30)
        self.rosterEntry.insert(0,self.rosterpathh)
        self.rosterEntry.pack(side=LEFT, padx=15, pady=10)

        rosterButton = Button(rosterFrame, command=self.rosterstartfilebrowser, text="Browse...")
        rosterButton.pack(side=LEFT, padx=28, pady=10)
        #DONE ROSTER FRAME

        #CREATING OUTPUT FRAME
        outputFrame = Frame(self)
        outputFrame.pack(fill=X, side=TOP)

        outputLabel = Label(outputFrame, text="Path to output:", background="white")
        outputLabel.pack(side=LEFT, padx=15, pady=10)

        self.outputEntry = Entry(outputFrame, width=30)
        self.outputEntry.insert(0,self.outpathh)
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
        self.teamsizeEntry.insert(0,self.teamsizeh)
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

    def optionUI(self):
        '''
        This creates the option window which
        presents the user with the generated
        teams and their options
        '''
        #RESETING WINDOW
        self.h = 400
        self.w = 800
        self.resetWindow()
        self.parent.title("Options")

        #CREATING SCROLL AREA
        scrollFrame = Frame(self)
        scrollFrame.pack(fill=X, side=TOP)

        self.teamlisting = Listbox(scrollFrame, width=self.w, height=18, \
                                selectmode=MULTIPLE)

        count = 1
        for team in self.interface.teams:
            teamstring  = "Team: " + str(count)
            teamstring += " score: " + "%.4f " % team.getRating()
            teamstring += " members: "
            for student in team.getMemberList():
                teamstring += student.getName() + " | "
            count += 1
            self.teamlisting.insert(END, teamstring)

        self.teamlisting.pack(padx=5, pady=5)
        #DONE SCROLL AREA

        #CREATING BOTTOM BUTTONS
        frame = Frame(self, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        backButton = Button(self,text="Back",command=self.startMainUI)
        backButton.pack(side=LEFT, padx=5, pady=5)
        exitButton = Button(self,text="Exit",command=lambda: self.parent.destroy() and exit())
        exitButton.pack(side=RIGHT, padx=5, pady=5)
        saveButton = Button(self,text="Save",command=self.interface.writeFile)
        saveButton.pack(side=RIGHT)
        rerunButton = Button(self,text="Rerun",command=self.reRun)
        rerunButton.pack(side=RIGHT, padx=5, pady=5)
        shuffleTeamsButton = Button(self,text="Shuffle Selected",command=self.shuffleSelected)
        shuffleTeamsButton.pack(side=RIGHT)
        swappingMembersButton = Button(self,text="Swap Members",command=self.memberSwap)
        swappingMembersButton.pack(side=RIGHT,padx=5, pady=5)
        emailscreenButton = Button(self,text="Email Team(s)",command=self.emailScreen)
        emailscreenButton.pack(side=RIGHT)
        #DONE BOTTOM BUTTONS

    def memberSwapUI(self,indexes):
        '''
        This creates the window which
        allows the user to swap
        individual members and reweigh
        teams.

        @param:
            indexes = int[]
        '''
        #RESETING WINDOW
        self.h = 400
        self.w = 800
        self.resetWindow()
        self.parent.title("Swapping Members")

        #CREATING SCROLL AREA
        scrollFrame = Frame(self)
        scrollFrame.pack(fill=X, side=TOP)

        self.teamlisting1 = Listbox(scrollFrame, width=self.w, height=9)

        self.teamlisting2 = Listbox(scrollFrame, width=self.w, height=9)

        count = 1
        team = self.interface.teams[indexes[0]]
        for student in team.getMemberList():
            teamstring = ""
            teamstring += student.getName()
            self.teamlisting1.insert(END, teamstring)
        count += 1

        team = self.interface.teams[indexes[1]]
        for student in team.getMemberList():
            teamstring = ""
            teamstring += student.getName()
            self.teamlisting2.insert(END, teamstring)
        count += 1

        self.teamlisting1.pack(padx=5, pady=5)
        self.teamlisting2.pack(padx=5, pady=5)
        #DONE SCROLL AREA

        #CREATING BOTTOM BUTTONS
        frame = Frame(self, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        backButton = Button(self,text="Back",command=lambda: self.swapSizeCheck(indexes))
        backButton.pack(side=LEFT, padx=5, pady=5)
        exitButton = Button(self,text="Exit",command=self.parent.destroy)
        exitButton.pack(side=RIGHT, padx=5, pady=5)
        swapButton = Button(self,text="Swap Team",command= lambda: self.switchTeams(indexes))
        swapButton.pack(side=RIGHT,padx=5, pady=5)
        #DONE BOTTOM BUTTONS

    def emailScreen(self):
        '''
        This starts the email login screen
        ''' 
        if(len(self.teamlisting.curselection()) < 1):
            messagebox.showinfo("Error","Please select one or more teams")
            return

        if(self.remember):
            self.emailTeams()
            return
            
        self.emailWindow = Toplevel(self.parent)
        self.centerWindow(self.emailWindow)

        #CREATING EMAIL FRAME
        emailFrame = Frame(self.emailWindow)
        emailFrame.pack(fill=X, side=TOP)  
        emailLabel = Label(emailFrame, text="Email address:", background="white")
        emailLabel.pack(side=LEFT, padx=15, pady=10)

        self.emailEntry = Entry(emailFrame, width=20)
        self.emailEntry.insert(0,"")
        self.emailEntry.pack(side=LEFT, padx=43, pady=10)
        #EMAIL FRAME DONE

        #CREATING PASSWORD FRAME
        passwordFrame = Frame(self.emailWindow)
        passwordFrame.pack(fill=X, side=TOP)  
        passwordLabel = Label(passwordFrame, text="Password:", background="white")
        passwordLabel.pack(side=LEFT, padx=17, pady=10)

        self.passwordEntry = Entry(passwordFrame, width=20, show="*")
        self.passwordEntry.insert(0,"")
        self.passwordEntry.pack(side=LEFT, padx=65, pady=10)
        #PASSWORD FRAME DONE

        #CREATING REMEMBER FRAME
        rememberFrame = Frame(self.emailWindow)
        rememberFrame.pack(fill=X, side=TOP)  
        rememberLabel = Label(rememberFrame, text="Remember Username/Password", background="white")
        rememberLabel.pack(side=LEFT, padx=15, pady=10) 

        self.rememberCheck = Checkbutton(rememberFrame)
        self.rememberCheck.pack(side=LEFT, padx=15, pady=10)
        #REMEMBER FRAME DONE

        #CREATING BOTTOM BUTTONS
        frame = Frame(self.emailWindow, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        exitButton = Button(self.emailWindow,text="Cancel",command=self.emailWindow.destroy)
        exitButton.pack(side=RIGHT, padx=5, pady=5)
        submitButton = Button(self.emailWindow,text="Submit",command=self.emailTeams)
        submitButton.pack(side=RIGHT,padx=5, pady=5)
        #DONE BOTTOM BUTTONS

    def emailTeams(self):
        '''
        This invokes emailing the selected teams
        '''
        success = True 

        if(not self.remember):
            selection = self.teamlisting.curselection() 
            email     = self.emailEntry.get()
            password  = self.passwordEntry.get()

            if(email == "" or password == ""):
                messagebox.showinfo("Error","Cannot leave fields empty")
                return

            if(len(self.rememberCheck.state()) != 0 and self.rememberCheck.state()[0] == "selected"):
                self.remember = True
                success = self.interface.sendEmail(selection,email,password,True)
            else:
                success = self.interface.sendEmail(selection,email,password)
                
        else:
           success = self.interface.sendEmail(self.teamlisting.curselection())

        if not success:
            self.remember = False
            messagebox.showinfo("Error","Sending the email was unsuccessful, check your email and password") 
            return

        if success:
            messagebox.showinfo("Success","Email was sent successfully") 
            self.emailWindow.destroy()
            return
             
    def loadingScreen(self):
        '''
        This starts the loading screen
        and disables all buttons
        '''
        for i in self.winfo_children():
            if Button == type(i):
                i.configure(state=DISABLED)

        self.loadWindow = Toplevel(self.parent)
        loadingstring   = "Please wait while we run the algorithm"
        loadinglabel    = Label(self.loadWindow, text=loadingstring, background="white")
        progressbar     = Progressbar(self.loadWindow, orient= "horizontal", \
                                    length=300, mode="indeterminate")
        progressbar.pack(pady=self.h/10)
        loadinglabel.pack()

        self.centerWindow(self.loadWindow)
        self.loadWindow.title("Wait")
        progressbar.start()

    def memberSwap(self):
        '''
        This will setup the call for memberSwapUI
        and check for improper/missing selections
        '''
        indexes = []
        selection = self.teamlisting.curselection()
        for i in selection:
            indexes.append(i)
        if len(indexes) == 2:
            self.memberSwapUI(indexes);
        else:
            messagebox.showinfo("Error","Please select 2 teams")

    def switchTeams(self, indexes):
        '''
        Puts selected members into the other team in
        the memberSwapUI
        @param:
            indexes = int[]
        '''
        student1 = self.teamlisting1.curselection()
        student2 = self.teamlisting2.curselection()

        if student1:
            if self.interface.teams[indexes[1]].getSize() < self.interface.teams[indexes[1]].getMaxSize():
                student = self.interface.teams[indexes[0]].getMemberByIndex(int(student1[0]))
                newTeam = self.interface.teams[indexes[1]]
                oldTeam = self.interface.teams[indexes[0]]
                newTeam.insertStudent(student)
                oldTeam.remStudent(student)
                self.memberSwapUI(indexes)
            else:
                messagebox.showinfo("Max Capacity", "Group is at maximum capacity")

        if student2:
            if self.interface.teams[indexes[0]].getSize() < self.interface.teams[indexes[0]].getMaxSize():
                student = self.interface.teams[indexes[1]].getMemberByIndex(int(student2[0]))
                newTeam = self.interface.teams[indexes[0]]
                oldTeam = self.interface.teams[indexes[1]]
                newTeam.insertStudent(student)
                oldTeam.remStudent(student)
                self.memberSwapUI(indexes)
            else:
                messagebox.showinfo("Max Capacity", "Group is at maximum capacity")

    def swapSizeCheck(self,indexes):
        '''
        This is a check to make sure before you back up from the
        memberSwapUI that the sizes are still correct

        @param:
            indexes = int[]
        '''
        if self.interface.teams[indexes[0]].getSize() < self.interface.teams[indexes[0]].getMinSize() \
                or self.interface.teams[indexes[1]].getSize() < self.interface.teams[indexes[1]].getMinSize():
            if messagebox.askokcancel("WARNING", "Warning: A group is shorthanded. You sure you want to proceed?"):
                for index in indexes:
                    self.interface.algorithm.weightCalc(self.interface.teams[index])
                self.optionUI();
        else:
            for index in indexes:
                self.interface.algorithm.weightCalc(self.interface.teams[index])
            self.optionUI();

    def shuffleSelected(self):
        '''
        This is a wrapper function that
        shuffles the selected teams
        '''
        #Gets selected values
        indexes   = []
        selection = self.teamlisting.curselection()
        for i in selection:
            indexes.append(i)

        self.interface.reShuffleSelectedTeams(indexes)
        self.optionUI()

    def reRun(self):
        '''
        A wrapper function to rerun the
        algorithm
        '''

        thread = ThreadedTask(self.queue,\
            self.interface.reShuffleAll)
        thread.start()
        ThreadedTask(self.queue,self.loadingScreen).start()
        self.checkThread(thread,self.optionUI)

    def submitFiles(self):
        '''
        Checks the validity of the entry feilds for
        After checks it runs our python script.
        '''
        csvtext     = self.csvEntry.get()
        teamsize    = self.teamsizeEntry.get()
        rostertext  = self.rosterEntry.get()
        outputtext  = self.outputEntry.get()

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
            messagebox.showinfo("Error","Please enter a positive integer for teamsize(2,5)")
            return

        self.csvpathh    = csvtext
        self.rosterpathh = rostertext
        self.outpathh    = outputtext
        self.teamsizeh   = teamsize

        self.interface.setOutputPath(outputtext)

        self.submitButton.configure(state=DISABLED)
        runalgorithm = lambda: self.interface.runGeneral(\
                        rostertext,csvtext,int(teamsize))
        thread1 = ThreadedTask(self.queue,runalgorithm)
        thread2 = ThreadedTask(self.queue,self.loadingScreen)
        thread2.start()
        thread1.start()

        self.checkThread(thread1,self.optionUI)

    def checkThread(self,thread,function):
        '''
        This function checks to see if
        the given thread is dead, if it
        is not, it recalls a new checkThread.
        After the thread is dead, it calls the
        given function

        @param:
            thread   - ThreadedTask
            functoin - a function
        '''
        if thread.is_alive():
            self.parent.after(1000, lambda: self.checkThread(thread,function))
        else:
            function()

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

class ThreadedTask(threading.Thread):
    '''
    Used for creating a threaded task
    '''
    def __init__(self,queue,function):
        '''
        Starts the threaded task

        @param:
            queue    - Queue object
            function - a function
        '''
        threading.Thread.__init__(self)
        self.queue    = queue
        self.function = function

    def run(self):
        '''
        Runs the function
        '''
        self.function()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', default='')
    parser.add_argument('-roster', default='')
    args = parser.parse_args()
    root = Tk()
    root.resizable(width=False, height=False)
    
    ex = Root(root, args.csv, args.roster)
    root.mainloop()

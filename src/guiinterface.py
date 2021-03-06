'''
@author Garett Roberts
created: Fri May 5 7:17:00 PDT 2017 
This is the Gui Interface for Team Builder.

Modifications:

Alister Maguire, Mon May  8 19:28:50 PDT 2017
Added the ConfigData argument to the algorithm manager. 

'''
from day         import Day
from team        import Team
from pathlib     import Path
from student     import Student
from inform      import send_email
from algorithm   import *
from iomanager   import IOManager
from config_data import ConfigData

class GuiInterface():
    '''
    The interface class
    '''
    def __init__(self):
        '''
        Initializes all items used by the
        interface to none
        '''
        self.teams      = None
        self.roster     = None
        self.c_data     = None
        self.manager    = None
        self.students   = None
        self.algorithm  = None
        self.outputpath = None
        self.email      = ""
        self.password   = ""
        self.saved      = False
    
    def loadRoster(self,rostertext):
        '''
        This loads the roster text file
        into a list of student names

        @param:
            rostertext: string
        '''
        self.roster = []
        with open(rostertext) as r_file:
            for line in r_file:
                self.roster.append(line) 

    def startManager(self):
        '''
        This starts the IOManager
        '''
        self.c_data  = ConfigData()
        self.manager = IOManager(self.c_data,self.roster)
    
    def readCsv(self,intext):
        '''
        This reads the csv file using
        the IOManager

        @param:
            intext: string
        '''
        self.students = self.manager.read(intext)
    
    def startAlgorithm(self,teamsize):
        '''
        This sets the teamsize for the algorithm
        and runs the algorithm
        
        @param:
            teamsize: int
        '''
        self.algorithm = AlgorithmManager(self.c_data, teamsize)
        self.teams     = self.algorithm.runMain(self.students)

    def runGeneral(self,rostertext,intext,teamsize):
        '''
        This sets and runs the guiinterface quickly

        @param:
            rostertext: string
            intext:     string
            teamsize:   int
        '''
        self.loadRoster(rostertext)
        self.startManager()
        self.readCsv(intext)
        self.startAlgorithm(teamsize)

    def setOutputPath(self,outputpath):
        '''
        This sets the outputpath

        @param:
            outputpath: string
        '''
        self.outputpath = outputpath

    def writeFile(self):
        '''
        This writes the file
        using the IOManager
        
        If file already exists,
        appends number to the end
        '''
        filenumber    = 1
        newoutputpath = self.outputpath + "/out.txt"
        newpath       = Path(newoutputpath)
        while(newpath.exists()):
            newoutputpath = self.outputpath + "/out" + str(filenumber) + ".txt"
            newpath       = Path(newoutputpath)
            filenumber   += 1
        self.manager.write(newoutputpath,self.teams)
    
    def reShuffleAll(self):
        '''
        This re-runs the algorithm fully to shuffle
        all of the teams
        '''
        self.teams = self.algorithm.runMain(self.students)

    def reShuffleTeams(self):
        '''
        This shuffles the teams using the swapMember
        algorithm from the Algorithm class
        '''
        self.teams = self.algorithm.swapMembers(self.teams) 

    def reShuffleSelectedTeams(self,indexes):
        '''
        This runs a teamswap on the selected teams.
        The selected teams are represented as indexes
        from the team object in the class

        @param:
            indexes: [int]
        '''
        swapping = []
        tempteam = [i for i in self.teams]

        for index in indexes:
            swapping.append(self.teams[index]) 
            tempteam.remove(self.teams[index])

        newteams = self.algorithm.swapMembers(swapping)
        for i in newteams:
            tempteam.append(i) 
        
        swapping = []
        self.teams = tempteam

    def sendEmail(self,teams,email="",password="",save=False):
        '''
        This emails the selected teams from the gui and 
        invokes the send_email method, the selected teams
        are represented as indexes corresponding to
        the teams within the self.teams list

        @param:
            teams    - [indexes] represents the teams at each index
            email    - string this is the email address given
            password - string that is the password
            save     - bool if true, will save the email and password until 
                           the end of the program     

        @returns:
            bool - True if success, False if failure 
        '''
        success = True

        if self.saved:
            for team in teams:
                success = send_email(self.teams[team],self.email,self.password)
                if not success:
                    return False 
            return True

        for team in teams:
            success = send_email(self.teams[team],email,password) 
            if not success:
                return False 

        if(save):
            self.email    = email
            self.password = password            
            self.saved    = True

        return True

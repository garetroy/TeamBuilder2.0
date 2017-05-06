'''
@author Garett Roberts
created: Fri May 5 7:17:00 PDT 2017

This is the Gui Interface for Team Builder.

'''
from day         import Day
from team        import Team
from pathlib     import Path
from student     import Student
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
        self.algorithm = AlgorithmManager(teamsize)
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
            indexes: [[int,int]...]
        '''
        swapping = []
        for item in indexes:
            swapping = []
            swapping.append(self.teams[item[0]])
            swapping.append(self.teams[item[1]])
            swapping = self.algorithm.swapMembers(swapping)
            self.teams[item[0]] = swapping[0]
            self.teams[item[1]] = swapping[1]
 
             


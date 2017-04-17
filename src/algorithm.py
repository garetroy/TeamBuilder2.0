'''
@author Garett Roberts
created: Sun Apr 15 12:51:00 PDT 2017

Algorithms creates a set of teams for the Team Builder.
It takes creates a random set of teams and weights them.

'''

from random import randrange
from student import Student
from team import Team

class AlgorithmManager():
    '''
    A algorithm manager for handling the team building
    '''

    def __init__(self):
        '''
            Initializes manager with the filter map, which maps the student
            prefrences to the corresponding functions to calculate the weights
            of the teams.

            @param:
                filter_dictionary: filterID's that map to functions

        '''

        self.__filter_dictionary = {"Meeting Times":(lambda s1,s2: 10)}

    '''
        Start Getters and Setters
    ''' 
    def getFilterDictionary(self):
        return self.__filter_dictionary

    def setFilterDictionary(self,fd):
        self.__filter_dictionary = fd

    def addFilter(self,filterin):
        '''
            Adds filters into the filter dictionary

            @param:
                filterin(string,function)
        '''
        self.__filter_dicitonary.append(filterin)

    '''
        End Getters and Setters
    '''

    def initTeamSet(self,students):
        '''
            Creates a TeamSet given a list of students
            Creates weights for each team
            
            @param:
                students([Student]) - a list of students

            @returns:
                [Team] - A set of teams  
        '''
        team_set = []
        team_in = Team()
        for s in range(len(students)):
            randnum = randrange(0,len(students))
            student = students.pop(randnum)
            team_in.insertStudent(student);
            if(team_in.getMaxSize() == team_in.getTeamSize()):
                self.weightCalc(team_in)
                team_set.append(team_in)
                team_in = Team()

        return team_set

    def weightCalc(self,team_in):
        '''
            Creates a weight for the team and sets the teams weight

            @param:
                team_in(Team) - A team
        '''
        team_in.setRating(0)
        for i in range(team_in.getTeamSize()-1):
            for j in range(i+1,team_in.getTeamSize()-1):
                team_in.setRating(team_in.getRating() + self.getWeight(team_in.getMemberByIndex(i),team_in.getMemberByIndex(j)))
    
    def getWeight(self, student1, student2):
        '''
            Creates a weight between two students
    
            @param:
                student1, student2 (Student) - Student
        '''
        total = 0
        for f in student1.getPrefs():
            total += self.getFilterDictionary()[f](student1,student2)  
        return total

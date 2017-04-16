'''
@author Garett Roberts
created: Sun Apr 15 12:51:00 PDT 2017

Algorithms creates a set of teams for the Team Builder.
It takes creates a random set of teams and weights them.

'''

from random import randint
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
                team_set: the set of teams we will manage
                filter_dictionary: filterID's that map to functions

        '''

        self.__team_set = []      
        slef.__filter_dictionary = {}

    
    def getTeamSet(self):
        return self.__team_set

    def getFilterDictionary(self):
        return self.__filter_dictionary

    def setTeamSet(self, fd):
        self.__team_set = ts 

    def setFilterDictionary(self,fd):
        self.__filter_dictionary = fd

    def addFilter(self,filterin):
        self.__filter_dicitonary.append(filterin)

    def addTeamSet(self, inteam):
        self.__team_set.append(inteam)

    def  init_team_set 

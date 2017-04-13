'''
@author: Alister Maguire
created: Thu Apr 13 15:21:27 PDT 2017

A filter which represents a teammate. 
'''
from tfilter import Filter

class Teammate(Filter):

    def __init__(self, name):
        '''
            Initialize a teammate. 

            @param:
                name: the name of the teammate
        '''
        self.__name = name

    def getName(self):
        '''
            Get the name of this teammate.

            @returns: the name of the teammate
        '''
        return self.__name

    def setName(self, name):
        '''
            Set the name of this teammate.

            @param:
                name: the name of the teammate
        '''
        self.__name = name

    def __eq__(self, other):
        '''
            Determine if two teammates are equal. Equality is 
            determined by comparing names, case-insensitive. 

            @param:
                other: a teammate to compare with this teammate. 
            @returns:
                True if other and this teammate share the same name. 
                False otherwise. 
        '''
        
        if not isinstance(other, Teammate):
            print("ERROR: cannot compare teammates with non-teammate type")
            return False

        if self.__name.lower() == other.__name.lower():
            return True
        return False
    
    def __str__(self):
        '''
            Get the string representation of a teammate. 
            
            @returns: 
                the name of this teammate. 
        '''
        return self.__name

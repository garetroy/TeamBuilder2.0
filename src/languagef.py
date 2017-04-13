'''
@author: Alister Maguire
created: Thu Apr 13 15:21:27 PDT 2017

A filter which represents a programming language. 
'''
from tfilter import Filter

class Language(Filter):

    def __init__(self, name):
        '''
            Initialize a language. 

            @param:
                name: the name of the teammate
        '''
        self.__name = name

    def getName(self):
        '''
            Get the name of this language.

            @returns: the name of the language
        '''
        return self.__name

    def setName(self, name):
        '''
            Set the name of this language.

            @param:
                name: the name of the language
        '''
        self.__name = name

    def __eq__(self, other):
        '''
            Determine if two languages are equal. Equality is 
            determined by comparing names, case-insensitive. 

            @param:
                other: a language to compare with this language. 
            @returns:
                True if other and this language share the same name. 
                False otherwise. 
        '''
        
        if not isinstance(other, Language):
            print("ERROR: cannot compare languages with non-language type")
            return False

        if self.__name.lower() == other.__name.lower():
            return True
        return False
    
    def __str__(self):
        '''
            Get the string representation of a language. 
            
            @returns: 
                the name of this language. 
        '''
        return self.__name

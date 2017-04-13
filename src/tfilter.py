'''
@author: Alister Maguire
created Thu Apr 13 15:21:27 PDT 2017

Filter is an abstract class that is to be inherited from
whenever creating a filter for grouping students. A 'filter'
is any criteria that is used to match students in groups; for
instance, 'available times to meet' is a criteria that can
be turned into a filter. 

'''
from abc import ABC, abstractmethod



class Filter(ABC):

    '''
        Retreive the name of this filter. 
    '''
    @abstractmethod
    def getName(self):
        pass

   
    '''
        Set the name of this filter. 
    '''
    @abstractmethod
    def setName(self):
        pass


    '''
        Define the equals operator for this filter. 
    '''
    @abstractmethod
    def __eq__(self):
        pass


    '''
        Define the str operator for this filter. 
    '''
    @abstractmethod
    def __str__(self):
        pass




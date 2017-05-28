'''
@author: Alister Maguire
create: Thu Apr 13 15:21:27 PDT 2017

IOManager is an object to handle IO for the Team Builder. 
As of now, the manager accepts csv files as input. Ideally, 
this module will allow for developers to easily extend the
types of input and output data used within the Team Builder. 


'''
from difflib import SequenceMatcher

import csv
import sys

class IOManager():
    '''
    A manager for handling IO for Team Builder. 
    '''

    def __init__(self, c_data, roster):
        '''
            Initialize the manager with an in type, an out type, 
            and a roster. 

            @param: 
                in_type: the type of input to be handled
                out_type: the type of output to be created
                roster: a list of valid student names in the following format;
 
                        ["last_name, first_name", ...]

        '''
       
        #associate reader/writer names with class methods for 
        #reading/writing that format
        self.c_data     = c_data
        self.__readers  = c_data.readers
        self.__writers  = c_data.writers

        self.__in_type  = c_data.defaults["rdr"]
        self.__out_type = c_data.defaults["wrtr"]
        self.__roster   = []
        self.__first_name_roster = [] #this is an optimization for error checking

        #populate roster
        for name in roster:
            parts = name.split(',')
            if len(parts) < 2 or len(parts) > 2:
                print("ERROR: roster format needs to be 'last name, first name'")
                sys.exit("Exiting: invalid roster")
            self.__roster.append(name.strip())
            self.__first_name_roster.append(parts[1].strip())


    def read(self, path):
        '''
            Select the appropriate reader to read a
            file for data collection.  

            @param:
                path: the path to the input file. 
            @returns:
                a list of Student objects. 
        '''
        return self.__readers[self.__in_type](self, path)


    def write(self, path, teams):
        '''
            Select the appropriate writer to write output data. 

            @param: 
                path: the path to the output file. 
        '''
        self.__writers[self.__out_type](self, path, teams) 


    def blockParser(self, block):
        '''
            Parse a contiguous block of csv data. These blocks 
            occur when there are multiple elements in a single 
            column and are often separated by semicolons. 

            @param:
                block: a block of csv data. 
            @returns:
                A list of the data from the csv block. 
        '''
        cpy = block.replace(';', ', ')
        return cpy.split(',')
            
    
    def nameChecker(self, name):
        '''
            Check to see if a name is valid. A name is considered
            valid if either of the following conditions are met:
                a. The full name is on the roster
                b. The first name is on the roster
                c. The full name is a 90% match to a name 
                   on the roster (spelling errors)

            @param: 
                name: a student name as a string. 
            @returns:
                A tuple such that the first element is a boolean 
                denoting whether or not a match was found and the 
                second element is the match that was found. NOTE:
                in cases of 90% match, the match from the roster
                is the name that is returned, not the given name.  
        '''

        #first, check to see if the input name
        #contains first and last name. If so, 
        #just search the roster for a match

        st_name = name.strip()

        if st_name == '':
            return (False, None)

        refined = ''
        if ' ' in st_name:
            if ',' not in st_name:
                #assuming that the name is 'first last' rather than 'last, first'
                parts   = st_name.split(' ')
                refined = parts[1] + ', ' + parts[0]
            else:
                refined = st_name
                
        elif ',' in st_name:
            #assuming they did not include space after comma
            parts   = st_name.split(',') 
            refined = parts[0] + ', ' + parts[1]

        if not refined == '':
            #If the name isn't in the roster, check for spelling errors. 
            #I'm accepting names that are a 90% match. 
            if refined not in self.__roster:
                for rname in self.__roster:
                    if SequenceMatcher(None, refined, rname).ratio() >= .9:
                        return (True, rname)
                print("refined name not found: " + refined)
                return (False, None)
            return (True, refined)
  
        #check for names that only have a first name
        else:
            count = self.__first_name_roster.count(name)
            if count == 1:
                limit = len(self.__roster)
                for i in range(limit):
                    parts = self.__roster[i].split(',')
                    if parts[1].strip() == name:
                        return (True, self.__roster[i])
                print("ERROR: couldn't find name match after knowing it exists?!")
                return (None, None)
            elif count > 1:
                print("ERROR: given first name only with several matches!")
                print("Omitting this student: " + name)
                return (None, None)
            else:
                print("name not found: " + name)
                return (False, None)
       
    

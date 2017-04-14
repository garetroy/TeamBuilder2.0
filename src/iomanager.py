'''
@author: Alister Maguire
create: Thu Apr 13 15:21:27 PDT 2017

IOManager is an object to handle IO for the Team Builder. 
As of now, the manager accepts csv files as input. Ideally, 
this module will allow for developers to easily extend the
types of input and output data used within the Team Builder. 


'''
from dayf import Day
from languagef import Language
from teammatef import Teammate
from student import Student
from difflib import SequenceMatcher

import csv
import sys

class IOManager():
    '''
    A manager for handling IO for Team Builder. 
    '''

    def __init__(self, roster, in_type='', out_type=''):
        '''
            Initialize the manager with an in type and an out type. 

            @param: 
                in_type: the type of input to be handled
                out_type: the type of output to be created
                roster: a list of valid student names in the following format;
 
                        ["last_name, first_name", ...]

        '''
       
        #TODO: we can scrap these lists and just use the 
        #      keys to the dictionaries below for checking.   
        self.__accepted_in  = ['csv', '']
        self.__accepted_out = ['txt', '']
        self.__roster       = []
        self.__first_name_roster = [] #this is an optimization for error checking

        if (in_type not in self.__accepted_in or
            out_type not in self.__accepted_out):
            print("ERROR: invalid in or out types declared...")
            print("The following types are currently accepted:")
            print("in: ", end='') 
            for t in self.__accepted_in:
                print(t, " ")
            print("out: ", end='') 
            for t in self.__accepted_out:
                print(t, " ")
            return None

        if in_type == '':
            self.__in_type  = 'csv'
        else:
            self.__in_type  = in_type

        if out_type == '':
            self.__out_type  = 'txt'
        else:
            self.__out_type  = out_type

        #associate reader/writer names with class methods for 
        #reading/writing that format
        self.__readers  = {'csv' : self.csvReader}
        self.__writers  = {'txt' : self.txtWriter}

        #populate roster
        for name in roster:
            parts = name.split(',')
            if len(parts) < 2 or len(parts) > 2:
                print("ERROR: roster format needs to be 'last name, first name'")
                sys.exit("Exiting: invalid roster")
            self.__roster.append(name)
            self.__first_name_roster.append(parts[1])



    def read(self, path):
        #TODO: finish the return value
        '''
            Select the appropriate reader to read a
            file for data collection.  

            @param:
                path: the path to the input file. 
            @returns:
                
        '''
        return self.__readers[self.__in_type](path)

    def csvReader(self, path):
        '''

            Current expected layout of csv file:

            Timestamp, name, email, mon, tues, wed, thurs, fri, sat, sun, lang, mate1, mate2

        '''
        students = []
      
        with open(path) as csvfile:
            lines = csv.reader(csvfile, delimiter=',', quotechar='"')
            #TODO: we should probably ensure that the data is in the 
            #      correct order or handle this is some better manner. 

            next(lines)
            for line in lines:
 
                #format the name, and check the roster for validity  
                splt = line[1].split(' ')
                if len(splt) > 1:
                    splt[0].strip()
                    splt[1].strip()
                    name = splt[1] + ', ' + splt[0]
                else:
                    name = splt[0].strip()

                result = self.nameChecker(name)
                
                #if the student is ambiguous or cannot be found, skip them
                if result[0] == None or result[0] == False:
                    continue

                name  = result[1]
                email = line[2] 
                times = []
                mates = []

                for i in range(3, 10):
                    if line[i] == '':
                        continue
                    times.append(self.blockParser(line[i]))

                lang  = self.blockParser(line[10])

                #TODO: there may be a better way of allowing
                #      extensions on the number of teammates. 
                for i in range(11, 13): 
                    mates.append(line[i])
               
                s = Student(name, email)
                #TODO: convert times to days, mates to teammates, and lang to 
                #      languages, and add them to the student

                students.append(s)

        return students
                

    def txtWriter(self, path):
        pass


    def blockParser(self, block):
        '''
        '''
        cpy = block.replace(';', ', ')
        return cpy.split(',')
            

    def nameChecker(self, name):
        '''
        '''
        #first, check to see if the input name
        #contains first and last name. If so, 
        #just search the roster for a match.
        if ',' in name:

            #If the name isn't in the roster, check for spelling errors. 
            #I'm accepting names that are a 90% match. 
            if name not in self.__roster:
                for rname in self.__roster:
                    if SequenceMatcher(None, name, rname).ratio() >= .9:
                        return (True, rname)
                print("name not found: " + name)
                return (False, None)
            return (True, name)
  
        #check for names that only have a first name
        else:
            count = self.__first_name_roster.count(name)
            if count == 1:
                limit = len(self.__roster)
                for i in range(limit):
                    parts = self.__roster[i].split(',')
                    if parts[1] == name:
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
       






    

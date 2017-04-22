'''
@author: Alister Maguire
create: Thu Apr 13 15:21:27 PDT 2017

IOManager is an object to handle IO for the Team Builder. 
As of now, the manager accepts csv files as input. Ideally, 
this module will allow for developers to easily extend the
types of input and output data used within the Team Builder. 


'''
from day import Day
from student import Student
from difflib import SequenceMatcher

import csv
import sys

class IOManager():
    '''
    A manager for handling IO for Team Builder. 
    '''

    def __init__(self, roster, in_type='csv', out_type='txt'):
        '''
            Initialize the manager with an in type, an out type, 
            and a roster. 

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
        self.__in_type      = in_type
        self.__out_type     = out_type
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
        return self.__readers[self.__in_type](path)


    def write(self, path, teams):
        '''
            Select the appropriate writer to write output data. 

            @param: 
                path: the path to the output file. 
        '''
        self.__writers[self.__out_type](path, teams) 


    def csvReader(self, path):
        '''
            Read data from a csv file and create Student objects from 
            this data. The format of the csv file is currently something
            that must be static. 
            Current expected layout of csv file:

                Timestamp, name, email, mon, tues, wed, thurs, fri, sat, sun, lang, mate1, mate2

            Maybe this can become more dynamic in the future.  
    
            @param:
                path: the path to the target csv file. 
            @returns:
                A list of Student objects. 
        '''
        students = []
      
        with open(path) as csvfile:
            lines = csv.reader(csvfile, delimiter=',', quotechar='"')
            #TODO: we should probably ensure that the data is in the 
            #      correct order or handle this is some better manner. 

            cols = next(lines)

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

                student = Student(result[1], line[2])
                filters = {}
                days    = []
                mates   = []

                for i in range(3, 10):
                    if line[i] == '':
                        day = Day(cols[i])
                        days.append(day)
                        continue
                    day = Day(cols[i])
                    int_times = list(map(lambda x : int(x), self.blockParser(line[i])))

                    for time in int_times:
                        day.insertTime(time)
                    days.append(day)
               
                #TODO: lets not hard code this
                #Filters are of the form (list, max list size, weight)
                filters['Schedule'] = (days, 13, 1)
                    
                lang_lst = self.blockParser(line[10])
                filters['Languages'] = (lang_lst, 3, 1)
                    
                #TODO: there may be a better way of allowing
                #      extensions on the number of teammates. 
                for i in range(11, 13): 
                    mate_tup = self.nameChecker(line[i])
                    if mate_tup[0]:
                        mates.append(mate_tup[1])
               
                filters['Teammates'] = (mates, 2, 1)
                student.setFilters(filters)
                students.append(student)

        return students

    def txtWriter(self, path, teams):
        '''
            The text file writer. This method merely pipes
            out the teams, there score, and the members of the
            teams to a text file. 

            @param:
                path: the path to write the text file to. 
                teams: a list of teams to be written. 
    
        '''
        with open(path, 'w') as out_file:
            count = 0
            for team in teams:
                out_str = ''
                members = team.getMemberList()
                out_file.write('Team ' + str(count) + '\n')
                out_file.write('score: ' + str(team.getRating()))
                out_file.write('\nmembers: \n') 
                #TODO: it would be great if we could write out 
                #      scores for each filter. 
                m_num = 1
                for student in members:
                    out_file.write(str(m_num) + ': ' + student.getName() + '\n') 
                    m_num += 1

                out_file.write('\n\n') 
                count += 1
                    

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
            return (True, name)
  
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
       
    

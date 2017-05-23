'''
@author: Alister Maguire

date: Sat May  6 11:25:50 PDT 2017

This file is used to store functions that read and write
student data. The functions within this file are used
by the iomanager.   

'''

import iomanager
import csv
from student import Student
from day import Day

def csvReader(iomanager, path):
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
 
        num_elements = 0#len(list(lines)[0])
        cols = next(lines)

        for line in lines:
            num_elements = (len(line)) if num_elements == 0 else num_elements
 
            #format the name, and check the roster for validity  
            splt = line[1].split(' ')
            if len(splt) > 1:
                splt[0].strip()
                splt[1].strip()
                name = splt[1] + ', ' + splt[0]
            else:
                name = splt[0].strip()

            result = iomanager.nameChecker(name)
                
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
                int_times = list(map(lambda x : int(x), iomanager.blockParser(line[i])))

                for time in int_times:
                    day.insertTime(time)
                days.append(day)
               
            #TODO: retrieving this data from the c_data is incredibly verbose
            #      and difficult to understand. Lets think about making this
            #      more accessible. 
            #Filters are of the form (list, max list size, weight)
            filters['Schedule'] = (days, iomanager.c_data.filter_dictionary['Schedule'][1], 
                                   iomanager.c_data.filter_dictionary['Schedule'][2])
                    
            lang_lst = iomanager.blockParser(line[10])
            filters['Languages'] = (lang_lst, iomanager.c_data.filter_dictionary['Languages'][1],
                                    iomanager.c_data.filter_dictionary['Languages'][2])
                    
            num_teammates = iomanager.c_data.filter_dictionary['Teammates'][1]
            start = num_elements - num_teammates

            for i in range(start, num_elements): 
                mate_tup = iomanager.nameChecker(line[i])
                if mate_tup[0]:
                    mates.append(mate_tup[1])
               
            filters['Teammates'] = (mates, num_teammates,
                                    iomanager.c_data.filter_dictionary['Teammates'][2])

            student.filters = filters
            students.append(student)

    return students


def txtWriter(iomanager, path, teams):
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
            members = team.members
            out_file.write('Team ' + str(count) + '\n')
            out_file.write('score: ' + str(team.rating))
            out_file.write('\nmembers: \n') 
            #TODO: it would be great if we could write out 
            #      scores for each filter. 
            m_num = 1
            for student in members:
                out_file.write(str(m_num) + ': ' + student.name + '\n') 
                m_num += 1

            out_file.write('\n\n') 
            count += 1


def scoreWriter(iomanager, path, teams):
    '''
        This is a writing method primarily used for testing and 
        debugging. It merely prints out the scores of each team. 

        @param:
            path: the path to write the text file to. 
            teams: a list of teams to be written. 
    
    '''
    with open(path, 'w') as out_file:
        count = 0
        for team in teams:
            out_str = ''
            members = team.members
            out_file.write('Team ' + str(count) + '\n')
            out_file.write('score: ' + str(team.rating))
            out_file.write('\n\n') 
            count += 1



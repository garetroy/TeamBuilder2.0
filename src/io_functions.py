'''
@author: Alister Maguire

This file is used to store functions that read and write
student data. The functions within this file are used
by the iomanager.   

'''

#the iomanager has useful static methods 
#to help with io. 
#from iomanager import IOManager
import iomanager

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

            result = IOManager.nameChecker(name)
                
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
                int_times = list(map(lambda x : int(x), IOManager.blockParser(line[i])))

                for time in int_times:
                    day.insertTime(time)
                days.append(day)
               
            #TODO: lets not hard code these filters.
            #      also, need to dynamically change
            #      weights from user input.  

            #Filters are of the form (list, max list size, weight)
            filters['Schedule'] = (days, 13, 1)
                    
            lang_lst = IOManager.blockParser(line[10])
            filters['Languages'] = (lang_lst, 3, 1)
                    
            #TODO: there may be a better way of allowing
            #      extensions on the number of teammates. 
            for i in range(11, 13): 
                mate_tup = IOManager.nameChecker(line[i])
                if mate_tup[0]:
                    mates.append(mate_tup[1])
               
            filters['Teammates'] = (mates, 2, 1)
            student.setFilters(filters)
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






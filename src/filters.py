'''
@author: Alister Maguire

This file is meant to hold filter algorithms used 
to match students. 


'''

from student import *

#WARNING:
#when setting to false, make sure to have the EXACT 
#format: 
#DEBUG = False
#This allows the test suite to replace for testing
DEBUG = False

def scheduleFilter(s1, s2):
    '''
        Given two students, look for common meeting times
        in there schedules and create a score based on this. 

        @param: 
            s1: student 1 
            s2: student 2 

        @returns:
            A score associated with these two students. 
    '''
    score = 0.0
    s1_schedule = s1.getPrefs()['Schedule'][0]
    s2_schedule = s2.getPrefs()['Schedule'][0]
    lst_max     = s2.getPrefs()['Schedule'][1]
    weight      = s2.getPrefs()['Schedule'][2]

    if DEBUG:
        print("Checking for schedule matching in students: " + 
               s1.getName() + " and " + s2.getName())

    inc = float(1.0/float(lst_max)) * float(weight)

    for day_idx in range(len(s1_schedule)):
    
        s1_day = s1_schedule[day_idx].getTimes()
        s2_day = s2_schedule[day_idx].getTimes()

        #First check if schdule overlaps exist    
        if s1_day == [] or s2_day == []:
            continue
        if not ( (s1_day[0] <= s2_day[-1] and s1_day[0] >= s2_day[0]) 
            or (s2_day[0] <= s1_day[-1] and s2_day[0] >= s1_day[0])):
            continue            

        i   = 0
        j   = 0

        s1_max = len(s1_day)
        s2_max = len(s2_day)

        #look for schedule matches
        while i < s1_max and j < s2_max:

            while s1_day[i] < s2_day[j] and i < (s1_max-1):
                i += 1
            while s2_day[j] < s1_day[i] and j < (s2_max-1):
                j += 1

            #TODO: this can be handled more efficiently
            if i == s1_max or j == s2_max:
                break
    
            if s1_day[i] == s2_day[j]:

                if DEBUG:
                    print("match: ")
                    print("  day: " + str(day_idx) + " time: " + str(s1_day[i]))

                score += inc
            j += 1

    #normalize
    score = float(score / float(len(s1_schedule)))

    if DEBUG:
        print("Total: " + str(score) + "\n\n")

    return score



def languageFilter(s1, s2):
    '''
        Given two students, compute a score associated 
        with how many cs languages they have in common. 

        @param: 
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students. 
    '''
    score = 0.0
    s1_lang = s1.getPrefs()['Languages'][0]
    s2_lang = s2.getPrefs()['Languages'][0]
    lst_max = s2.getPrefs()['Languages'][1]
    weight  = s2.getPrefs()['Languages'][2]

    inc = float(1.0/float(lst_max)) * float(weight)

    for lang in s1_lang:
        if lang in s2_lang:
            score += inc

    return score



def teammateFilter(s1, s2):
    '''
        Associate a score with two students regarding whether 
        or not they want to work with eachother. 

        @param:
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students. 
    '''
    score = 0.0
    s1_mates = s1.getPrefs()['Teammates'][0]
    s2_mates = s2.getPrefs()['Teammates'][0]
    lst_max  = s2.getPrefs()['Teammates'][1]
    weight   = s2.getPrefs()['Teammates'][2]

    inc = float(1.0/float(lst_max)) * float(weight)

    if s1.getName() in s2_mates:
        score += inc
    if s2.getName() in s1_mates:
        score += inc

    return score







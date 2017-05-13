'''
@author: Alister Maguire
date: Sun Apr 23 16:48:05 PDT 2017

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
            A score associated with these two students between 0 and 1.
    '''
    score = 0.0
    s1_schedule = s1.getPrefs()['Schedule'][0]
    s2_schedule = s2.getPrefs()['Schedule'][0]
    #lst_max     = s2.getPrefs()['Schedule'][1]
    weight      = s2.getPrefs()['Schedule'][2]

    #get maximum schedule len for normalizing
    #in other words, what is the largest number of 
    #possible overlaps between these two students
    #if they both had identical, maximum schedules?

    if DEBUG:
        print("Checking for schedule matching in students: " + 
               s1.getName() + " and " + s2.getName())

    for day_idx in range(len(s1_schedule)):
        s1_times = s1_schedule[day_idx].getTimes()
        s2_times = s2_schedule[day_idx].getTimes()

        if s1_times == [] or s2_times == []:
            continue

        min_times = s1_times if s1_times < s2_times else s2_times 
        max_times = s1_times if s1_times > s2_times else s2_times 
        inc = float(1.0/float(len(min_times))) * float(weight)

        for time in min_times:
            if time in max_times:
                if DEBUG:
                    print("MATCH: ", str(time))
                score += inc

     
    score = float(score / float(len(s1_schedule)))

    if DEBUG:
        print("Total: " + str(score) + "\n\n")

    if score > 1.0:
        print("ERROR: schedule score is greater than 1!!") 

    return score



def languageFilter(s1, s2):
    '''
        Given two students, compute a score associated 
        with how many cs languages they have in common. 

        @param: 
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students between 0 and 1.
    '''
    score = 0.0
    s1_lang = s1.getPrefs()['Languages'][0]
    s2_lang = s2.getPrefs()['Languages'][0]
    weight  = s2.getPrefs()['Languages'][2]

    #get maximum list len for normalizing
    #in other words, what is the largest number of 
    #possible overlaps between these two students
    #if they had identical preferences?
    s1_len  = len(s1_lang)
    s2_len  = len(s2_lang)
    max_len = s1_len if s1_len > s2_len else s2_len

    inc = float(1.0/float(max_len)) * float(weight)

    if DEBUG:
        print("Checking for language matching in students: " + 
               s1.getName() + " and " + s2.getName())

    for lang in s1_lang:
        if lang in s2_lang:
            score += inc
            if DEBUG:
                print("match: ")
                print("   lang: " + lang)

    if DEBUG:
        print("score: " + str(score) + "\n\n")
    if score > 1.0:
        print("ERROR: language score is greater than 1!!") 

    return score



def teammateFilter(s1, s2):
    '''
        Associate a score with two students regarding whether 
        or not they want to work with eachother. 

        @param:
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students between 0 and 1.
    '''
    score = 0.0
    s1_mates = s1.getPrefs()['Teammates'][0]
    s2_mates = s2.getPrefs()['Teammates'][0]
    weight   = s2.getPrefs()['Teammates'][2]

    #since we are comparing two students, we add .5 
    #each time one of them wants to work with the other
    #for a maximum score of 1. 
    inc = 0.5

    if DEBUG:
        print("Checking for teammate matching in students: " + 
               s1.getName() + " and " + s2.getName())

    if s1.getName() in s2_mates:
        score += inc
        if DEBUG:
            print("match: ")
            print(s2.getName() + " wants to work with " + s1.getName())

    if s2.getName() in s1_mates:
        score += inc
        if DEBUG:
            print("match: ")
            print(s1.getName() + " wants to work with " + s2.getName())

    if DEBUG:
        print("score: " + str(score) + "\n\n")

    if score > 1.0:
        print("ERROR: teammate score is greater than 1!!") 

    return score







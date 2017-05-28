'''
@author: Alister Maguire
date: Sun Apr 23 16:48:05 PDT 2017

This file is meant to hold filter algorithms used 
to match students. 


IMPORTANT:
All filter functions must have exactly two parameters
(two student objects), and each filter must return a 
floating point value between 0 and 1 inclusive which
represents the match between students. 


'''
import os
import sys

#grab the path to the src folder
curpth    = os.path.dirname(os.path.abspath(__file__))
targetpth = curpth + '/../src/'
sys.path.insert(0, targetpth)

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
            A score associated with these two students between 0.0 and 
            the weight associated with this filter. 
    '''
    score = 0.0
    s1_schedule = s1.filters['Schedule'][0]
    s2_schedule = s2.filters['Schedule'][0]
    weight      = s2.filters['Schedule'][2]
    total_days  = len(s1_schedule)

    #get maximum schedule len for normalizing
    #in other words, what is the largest number of 
    #possible overlaps between these two students
    #if they both had identical, maximum schedules?

    if DEBUG:
        print("Checking for schedule matching in students: " + 
               s1.name + " and " + s2.name)

    for day_idx in range(len(s1_schedule)):
        s1_times = s1_schedule[day_idx].times
        s2_times = s2_schedule[day_idx].times

        if s1_times == [] or s2_times == []:
            total_days -= 1
            continue

        s1_t_size = len(s1_times)
        s2_t_size = len(s2_times)
        min_times = s1_times if s1_t_size < s2_t_size else s2_times 
        max_times = s1_times if s1_t_size > s2_t_size else s2_times 
        inc = float(weight)/float(len(min_times))

        for time in min_times:
            if time in max_times:
                if DEBUG:
                    print("MATCH: ", str(time))
                score += inc

    score = float(score / float(total_days))

    if DEBUG:
        print("Total: " + str(score) + "\n\n")

    if score > weight:
        print("ERROR: schedule score is greater than weight!!") 

    return score



def languageFilter(s1, s2):
    '''
        Given two students, compute a score associated 
        with how many cs languages they have in common. 

        @param: 
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students between 0.0 and 
            the weight associated with this filter. 
    '''
    score = 0.0
    s1_lang = s1.filters['Languages'][0]
    s2_lang = s2.filters['Languages'][0]
    weight  = s2.filters['Languages'][2]

    #get maximum list len for normalizing
    #in other words, what is the largest number of 
    #possible overlaps between these two students
    #if they had identical preferences?
    s1_len  = len(s1_lang)
    s2_len  = len(s2_lang)
    max_len = s1_len if s1_len > s2_len else s2_len

    inc = float(float(weight)/float(max_len))

    if DEBUG:
        print("Checking for language matching in students: " + 
               s1.name + " and " + s2.name)

    for lang in s1_lang:
        if lang in s2_lang:
            score += inc
            if DEBUG:
                print("match: ")
                print("   lang: " + lang)

    if DEBUG:
        print("score: " + str(score) + "\n\n")
    if score > weight:
        print("ERROR: language score is greater than weight!!") 

    return score



def teammateFilter(s1, s2):
    '''
        Associate a score with two students regarding whether 
        or not they want to work with eachother. 

        @param:
            s1: student 1
            s2: student 2

        @returns:
            A score associated with these two students between 0.0 and 
            the weight associated with this filter. 
    '''
    score = 0.0
    s1_mates = s1.filters['Teammates'][0]
    s2_mates = s2.filters['Teammates'][0]
    weight   = s2.filters['Teammates'][2]

    #since we are comparing two students, we add .5 
    #each time one of them wants to work with the other
    #for a maximum score of 1. 
    inc = 0.5*float(weight)

    if DEBUG:
        print("Checking for teammate matching in students: " + 
               s1.name + " and " + s2.name)

    if s1.name in s2_mates:
        score += inc
        if DEBUG:
            print("match: ")
            print(s2.name + " wants to work with " + s1.name)

    if s2.name in s1_mates:
        score += inc
        if DEBUG:
            print("match: ")
            print(s1.name + " wants to work with " + s2.name)

    if DEBUG:
        print("score: " + str(score) + "\n\n")

    if score > weight:
        print("ERROR: teammate score is greater than weight!!") 

    return score







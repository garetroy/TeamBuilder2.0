'''
@author: Garett Roberts

Algorithm testing

'''
import os
import argparse
import sys
#for bypassing import paths
curpth     = os.path.dirname(os.path.abspath(__file__))
targetpth1 = curpth + '/../../src/'
targetpth2 = curpth + '/../../config/'
sys.path.insert(0, targetpth1)
sys.path.insert(0, targetpth2)

from team import Team
from day import Day
from student import Student
from algorithm import AlgorithmManager

if __name__ == "__main__":
    algorithm  = AlgorithmManager()
    studentlis = []

    d1 = Day("Tuesday")
    d1.insertTime(10)
    d1.insertTime(13)    
    d2 = Day("Wednesday")
    d2.insertTime(10)
    d2.insertTime(14)

    s1 = Student("Hope, Bob","mahananaka@gmail.com")
    days = [d1, d2]
    filters1 = {}
    filters1['Meeting Times'] = days
    s1.setFilters(filters1)
    studentlis.append(s1)

    s2 = Student("Jensen, Emily","")
    days = [d2]
    filters2 = {}
    filters2['Meeting Times'] = days
    s2.setFilters(filters2)
    studentlis.append(s2)

    d1 = Day("Tuesday")
    d1.insertTime(10)
    d1.insertTime(13)    
    d2 = Day("Wednesday")
    d2.insertTime(10)
    d2.insertTime(14)

    s3 = Student("Streisand, Barbara","")
    days = [d1,d2]
    filters3 = {}
    filters3['Meeting Times'] = days
    s3.setFilters(filters3)
    studentlis.append(s3)

    s4 = Student("Cobain, Curt","")
    days = [d2]
    filters4 = {}
    filters4['Meeting Times'] = days
    s4.setFilters(filters4)
    studentlis.append(s4)

    s5 = Student("Dog, Man", "")
    days = [d2]
    filters5 = {}
    filters5['Meeting Times'] = days
    s5.setFilters(filters5)
    studentlis.append(s5)
        
    teamset = algorithm.initTeamSet(studentlis)

    [print(i.getRating()) for i in teamset] 

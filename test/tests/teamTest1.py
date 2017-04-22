'''
@author: Alister Maguire

Basic test for the IOManager object.

'''
import os
import argparse
import sys

#python doesn't allow fo importing modules from other
#directories, so I'm bypassing this. 
curpth    = os.path.dirname(os.path.abspath(__file__))
targetpth = curpth + '/../../src/'
sys.path.insert(0, targetpth)

from iomanager import IOManager
from team import Team
from day import Day
from student import Student
from algorithm import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    parser.add_argument('roster_path')
    parser.add_argument('output_path')
    args       = parser.parse_args()
    csv_pth    = args.csv_path
    roster_pth = args.roster_path
    out_path   = args.output_path
    roster     = []

    #grab the roster file and create a roster list
    with open(roster_pth) as r_file:
        for line in r_file:
            roster.append(line)
    '''
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

    s2 = Student("Jensen, Emily","")
    days = [d2]
    filters2 = {}
    filters2['Meeting Times'] = days
    s2.setFilters(filters2)


    t1 = Team(2,4)
    t1.insertStudent(s1)
    t1.insertStudent(s2)

    d1 = Day("Tuesday")
    d1.insertTime(10)
    d1.insertTime(13)    
    d2 = Day("Wednesday")
    d2.insertTime(10)
    d2.insertTime(14)

    s1 = Student("Streisand, Barbara","")
    days = [d1,d2]
    filters3 = {}
    filters3['Meeting Times'] = days
    s1.setFilters(filters3)

    s2 = Student("Cobain, Curt","")
    days = [d2]
    filters4 = {}
    filters4['Meeting Times'] = days
    s2.setFilters(filters4)

    t2 = Team(2,4)

    t2.insertStudent(s1)
    t2.insertStudent(s2)

    team_lst = [t1, t2]
    '''

    manager  = IOManager(roster)
    students = manager.read(csv_pth)
    alg      = AlgorithmManager()
    teams    = alg.runMain(students)
    manager.write(out_path, teams)
   




    

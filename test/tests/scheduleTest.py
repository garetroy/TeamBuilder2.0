'''
@author: Alister Maguire

A basic test for the schedule matching algorithm. 
'''

import os
import argparse
import sys
import fileinput

#python doesn't allow fo importing modules from other
#directories, so I'm bypassing this. 
curpth    = os.path.dirname(os.path.abspath(__file__))
targetpth = curpth + '/../../src/'
sys.path.insert(0, targetpth)
filter_file = targetpth + 'filters.py'

#turn debugging on in the filter file
with fileinput.FileInput(filter_file, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("DEBUG = False", "DEBUG = True"), end='')

from filters import *
from iomanager import *
from config_data import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    parser.add_argument('roster_path')
    args       = parser.parse_args()
    csv_pth    = args.csv_path
    roster_pth = args.roster_path
    roster     = []

    #grab the roster file and create a roster list
    with open(roster_pth) as r_file:
        for line in r_file:
            roster.append(line)

    c_data = ConfigData()

    manager = IOManager(c_data, roster)
    students = manager.read(csv_pth)


    for i in range(0, 18, 2):
        scheduleFilter(students[i], students[i+1])
            

    #turn off debugging in the filter file
    with fileinput.FileInput(filter_file, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("DEBUG = True", "DEBUG = False"), end='')



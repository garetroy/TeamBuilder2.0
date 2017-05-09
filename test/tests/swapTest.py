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
from config_data import *

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

    c_data = ConfigData()

    manager  = IOManager(c_data, roster)
    students = manager.read(csv_pth)
    alg      = AlgorithmManager()
    teams    = alg.runMain(students)
    manager.write(out_path, teams)
   




    

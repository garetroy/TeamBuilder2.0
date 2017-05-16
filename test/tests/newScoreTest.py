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

from filters import *
from iomanager import *
from config_data import *
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

    c_data = ConfigData()

    #grab the roster file and create a roster list
    with open(roster_pth) as r_file:
        for line in r_file:
            roster.append(line)

    manager  = IOManager(c_data, roster, 'csv', 'score')
    students = manager.read(csv_pth)
    alg      = AlgorithmManager(c_data)
    teams    = alg.runMain(students)

    manager.write(out_path, teams)

            



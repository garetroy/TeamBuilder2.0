'''
@author: Alister Maguire
date: Sun Apr 23 16:48:05 PDT 2017
This is the main module for running the team builder
program from the command line. 
@command line args:
    csv_path: a path to an input csv file.
    roster_path: a path to an input roster.
    output_path: a path to the desired output file.  
    team_size: the minumum desired team size.
'''

import argparse
from iomanager import IOManager
from team import Team
from day import Day
from student import Student
from algorithm import *
fromt config_data import ConfigData

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run the team building algorithm')
    parser.add_argument('csv_path', type=str, help='''the path to a csv file
                         containing student survey data''')
    parser.add_argument('roster_path', type=str, help='''the path to a student 
                         roster file''')
    parser.add_argument('output_path', type=str, help='''name and path of the 
                         output file containing the resulting teams''')
    parser.add_argument('team_size', type=int, help='''the minimum team size''')

    args       = parser.parse_args()
    t_size     = args.team_size
    csv_pth    = args.csv_path
    roster_pth = args.roster_path
    out_path   = args.output_path
    roster     = []

    #create an objec to hold the config data. 
    c_data = ConfigData()

    #grab the roster file and create a roster list
    with open(roster_pth) as r_file:
        for line in r_file:
            roster.append(line)

    #create the io manager
    manager  = IOManager(c_data, roster)
    students = manager.read(csv_pth)

    #run the algorithm
    alg      = AlgorithmManager(t_size)
    teams    = alg.runMain(students)

    #write the output teams
    manager.write(out_path, teams)
   

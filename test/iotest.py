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
targetpth = curpth + '/../src/'
sys.path.insert(0, targetpth)

from iomanager import IOManager

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

    manager = IOManager(roster)
    students = manager.read(csv_pth)

    print('students:')
    for s in students:
        print(s)
   
    




    

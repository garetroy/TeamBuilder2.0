'''
@author Garett Roberts
created: Sun Apr 15 12:51:00 PDT 2017

Algorithms creates a set of teams for the Team Builder.
It takes creates a random set of teams and weights them.

Modifications:

Alister Maguire, Sat Apr 22 10:18:00 PDT 2017 
Added filters to the algorithm. Changed the 
weightCalc to account for the normalization. 
Fixed a bug in the main algorithm. Experimented
with changing k, d, and n values. 

Alister Maguire, Sun Apr 23 12:54:54 PDT 2017
extended initTeamSet to handle students that
don't fit nicely into the group sizes. 

Alister Maguire, Mon May  8 19:28:50 PDT 2017
Added the dynamic setting of the filter dictionary
by the config data. 

Alister Maguire, Sat May 13 17:18:42 PDT 2017
fixed bug in the swapMembers method. 

Alister Maguire, Mon May 15 20:50:22 PDT 2017
fixed bug in the runMain.

Alister Maguire, Tue May 16 16:33:18 PDT 2017
Improved algorithm's ability to find optimized
teams.

'''
import os
import sys

#grab the path to the config folder
curpth    = os.path.dirname(os.path.abspath(__file__))
targetpth = curpth + '/../config/'
sys.path.insert(0, targetpth)

from random import randrange
from student import Student
from team import Team
from filters import *
from swap_list import SwapList

DEBUG = False

class AlgorithmManager():
    '''
    A algorithm manager for handling the team building
    '''

    def __init__(self, c_data, team_size=3, k=10,d=20,n=25):
        '''
            Initializes manager with the filter map, which maps the student
            prefrences to the corresponding functions to calculate the weights
            of the teams.

            @param:
                filter_dictionary: filterID's that map to functions

        '''
        self.filter_dictionary = {}

        for filt in c_data.filter_dictionary:
            self.filter_dictionary[filt] = c_data.filter_dictionary[filt][0]
            
        self.__team_size         = team_size
        self.k                   = k
        self.d                   = d
        self.n                   = n

    '''
        Start Getters and Setters
    ''' 
    def getFilterDictionary(self):
        return self.filter_dictionary

    def setFilterDictionary(self,fd):
        self.filter_dictionary = fd

    def addFilter(self,filterin):
        '''
            Adds filters into the filter dictionary

            @param:
                filterin(string,function)
        '''
        self.__filter_dicitonary.append(filterin)

    '''
        End Getters and Setters
    '''

    def initTeamSet(self,students):
        '''
            Creates a TeamSet given a list of students
            Creates weights for each team
            
            @param:
                students([Student]) - a list of students

            @returns:
                [Team] - A set of teams  
        '''
        studentlist = SwapList(i for i in students)
        team_set    = SwapList()
        team_in     = Team(self.__team_size, self.__team_size + 1)
        for s in range(len(studentlist)):
            student = studentlist.swapPop(randrange(0, len(studentlist)))
            team_in.insertStudent(student)
            if(team_in.minsize == team_in.getTeamSize()):
                self.weightCalc(team_in)
                team_set.append(team_in)
                team_in = Team(self.__team_size, self.__team_size + 1)

        t_max     = team_in.maxsize
        num_extra = team_in.getTeamSize()
        if num_extra < t_max:
            if num_extra > len(team_set):
                print(""""ERROR: there are too many excess students for the team
                          sizes you have chosen for this class size. Try 
                          re-thinking team sizes""")
                sys.exit(0)
            leftovers = team_in.members
            idx = 0
            while leftovers:
                team_set[idx].insertStudent(leftovers.pop())    
                self.weightCalc(team_set[idx])
                idx = (idx + 1) if (idx < t_max) else 0
        return team_set

    def weightCalc(self,team_in):
        '''
            Creates a weight for the team and sets the teams weight

            @param:
                team_in(Team) - A team
        '''
        team_in.rating = 0.0
        size   = team_in.getTeamSize()
        denom  = 0
        weight = 0.0
        for i in range(size):
            for j in range(i+1, size):
                denom  += 1
                weight += self.getWeight(team_in.members[i],team_in.members[j])

        #Normalize the weights
        weight = weight / denom
        team_in.rating = weight
    
    def getWeight(self, student1, student2):
        '''
            Creates a weight between two students
    
            @param:
                student1, student2 (Student) - Student
            
            @returns:
                total (int) - the rating of two students
        '''
        total = 0.0
        for f in student1.filters:
            total += self.filter_dictionary[f](student1,student2)  

        total = total/len(self.filter_dictionary)

        return total

    def swapMembers(self,teams):
        '''
            Swaps members within teams and re-calculates ratings

            @param:
                teams: [Team] - a list of teams
            
            @returns:
                teams: [Team] - swapped teams
        '''
        size = len(teams)

        if(size == 1):
            new_teams = SwapList()
            new_t = Team()
            new_t.deepCopy(teams[0])
            new_teams.append(new_t)
            return teams

        if DEBUG:
            print("\n\nin teams: ")
            for t in teams:
                print("**")
                print(t)
                print("**")

        #need to create new teams to move members around
        new_teams = SwapList()
        for i in range(size):
            new_t = Team()
            new_t.deepCopy(teams[i])
            new_teams.append(new_t)
            
        for i in range(size):
            swp_idx = i
            while swp_idx == i:
                swp_idx = randrange(size)
                
            s1_list = new_teams[i].members
            s2_list = new_teams[swp_idx].members

            #TODO: this can end up swapping the same
            #      members back and forth => nothing
            #      actually changes. It's rare, but we 
            #      can prevent this with some caching.  
            s1 = s1_list.swapPop(randrange(len(s1_list)))
            s2 = s2_list.swapPop(randrange(len(s2_list)))
 
            new_teams[i].members.append(s2)
            new_teams[swp_idx].members.append(s1)

            self.weightCalc(new_teams[i])
            self.weightCalc(new_teams[swp_idx])

        if DEBUG:
            print("\n\nout teams: ")
            for t in new_teams:
                print("**")
                print(t)
                print("**")

        return new_teams

    def groupScore(self,teams):
        '''
            This method creates a score associated with a 'group' of teams. 
            The score is found by subtracting the 'deviation' from the 
            total score of all the teams in the group. Deviation here is
            defined has the 'highest team score' - 'lowest team score'. 

            @params:
                teams: [Team]
            
            @returns:
                group_score, as defined above. 
        '''
        max_idx = 0
        min_idx = 0
        total_score = 0.0

        #calculate find the highest and lowest scoring groups and
        #sum up all of the scores. 
        for i in range(len(teams)):
            cur_score    = teams[i].rating
            total_score += cur_score
            if cur_score > teams[max_idx].rating:
                max_idx = i
            if cur_score < teams[min_idx].rating:
                min_idx = i

        #calculate the deviation and group score
        dev = teams[max_idx].rating - teams[min_idx].rating
        group_score = total_score - dev

        return group_score

    def runMain(self,students):
        '''
            Creates k different sets of teams, then finds the teams and swaps them around
            until we get an "evened" out team set
        
            @params:
                students [Student] - a list of all the students
        '''
        grouping_list = SwapList() 

        for _ in range(self.k):
            grouping_list.append(self.initTeamSet(students))

        #here is the heart of the algorithm. We randomly swap 
        #members and create new teams, picking out the best 
        #teams and putting them back into our swapping pool.
        for _ in range(self.d):
            for _ in range(self.k):
                variants = SwapList()

                teams = grouping_list.swapPop(randrange(len(grouping_list)))

                variants.append(teams)
                for _ in range(self.n - 1):
                    variants.append(self.swapMembers(teams))

                max_score = -1
                max_idx   = 0
               
                #find the highest scoring group in our list of 
                #groups, and append this back to the main grouping 
                #list. 
                for m in range(self.n - 1):
                    grp_score = self.groupScore(variants[m]) 
                 
                    if grp_score > max_score:
                        max_score = grp_score
                        max_idx   = m
                grouping_list.append(variants[max_idx])

        max_score = -1
        max_idx   = 0

        #Return the group with the highest score. 
        for i in range(self.k):
            grp_score = self.groupScore(grouping_list[i])
            if grp_score > max_score:
                max_score = grp_score
                max_idx = i
        return grouping_list[max_idx]

'''
Written by Jared Paeschke, jpaeschk@uoregon.edu
Course: CIS 422 Spring 2017

This class is part of a team project to make a team formation automater &
optimizer. Project members include Alister Maguire, Jared Paeschke, & 
Garett Roberts.

Modifications:

Alister Maguire, Fri Apr 14 17:37:51 PDT 2017 
Added a method for retrieving a list of team 
members called getMemberList.

Garett Roberts, Sun Apr 16 17:30:00 PDT 2017
Simplified insertStudent function and removed accidentially
commented out functions 

Alister Maguire, Sat Apr 22 14:18:37 PDT 2017
Changed the type check in 'setRating' from int
to float.

Alister Maguire, Sun May  7 17:34:01 PDT 2017
Added a method to retrieve the actual team size. 

Alister Maguire, Mon May 15 19:48:23 PDT 2017
Corrected score weight. And fixed bug in 
deepCopy.

Jared Paeschke, Tue May 30 21:05:44 2017
Removed use of getters and setters
'''

from student import Student
from day import Day
from swap_list import SwapList

class Team:

	#constructor
	def __init__(self, minimum=3, maximum=4):
		self.members = SwapList()
		self.minsize = minimum
		self.maxsize = maximum
		self.rating = 0.0

	def deepCopy(self, other):
		if not isinstance(other, Team):
			return

		for member in other.members:
			self.members.append(member)
		self.minsize = other.minsize
		self.maxsize = other.maxsize
		self.rating = other.rating

	#returns current number of team members
	def getTeamSize(self):
		return len(self.members)

	#adds a Student to the team, only allows Student objects
	#if student is found in the list it is not added. returns
	#true or false depending on successful insert.
	def insertStudent(self, s):
		if len(self.members) >= self.maxsize:
			return False

		if type(s).__name__ != "Student":
			return False

		for member in self.members:
			if s == member:
				return False 


		self.members.append(s)
		return True

	#removes a student from the team. returns true
	#if action was successful, false otherwise.
	def remStudent(self, s):
		if type(s).__name__ != "Student":
			return False

		for i in range(len(self.members)):
			if s == self.members[i]:
				del self.members[i]
				return True

		return False

	#purges the list of members on this team. also affects
	#anything that references to this value. (exampel:
	#cpy = self.__members; cpy will be purged too)
	def purgeMembers(self):
		del self.members[:]

	#determines if two teams are equivalent
	def __eq__(self,other):
		if len(self.members) != len(other.members):
			return False

		for i in range(len(self.members)):
			if self.members[i] != other.members[i]:
				return False
		return True

	#represents the team object as a string
	def __str__(self):
		output = ""
		for i in range(len(self.members)):
			output += str(self.members[i]) + "\n"

		return output[:-1]

#tester function the Team class, only runs when this module is main
def test_team():

	s1 = Student("Jared Paeschke","mahananaka@gmail.com")

	s2 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
	
	t = Team(3,4)
	print("t.insertStudent(s1): " + str(t.insertStudent(s1)))
	print("t.insertStudent(s1): " + str(t.insertStudent(s1)))
	print("t.insertStudent(s2): " + str(t.insertStudent(s2)))

	print(t)

if __name__ == "__main__":
	test_team()

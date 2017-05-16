##
#
# Written by Jared Paeschke, jpaeschk@uoregon.edu
# Course: CIS 422 Spring 2017
#
# This class is part of a team project to make a team formation automater &
# optimizer. Project members include Alister Maguire, Jared Paeschke, & 
# Garett Roberts.
#
# Modifications:
#
# Alister Maguire, Fri Apr 14 17:37:51 PDT 2017 
# Added a method for retrieving a list of team 
# members called getMemberList.
#
# Garett Roberts, Sun Apr 16 17:30:00 PDT 2017
# Simplified insertStudent function and removed accidentially
# commented out functions 
#
# Alister Maguire, Sat Apr 22 14:18:37 PDT 2017
# Changed the type check in 'setRating' from int
# to float.
#
# Alister Maguire, Sun May  7 17:34:01 PDT 2017
# Added a method to retrieve the actual team size. 
#
# Alister Maguire, Mon May 15 19:48:23 PDT 2017
# Corrected score weight. And fixed bug in 
# deepCopy.
##

from student import Student
from day import Day

class Team:

	#constructor
	def __init__(self, minimum=3, maximum=4):
		self.__members = []
		self.__minsize = minimum
		self.__maxsize = maximum
		self.__rating = 0.0

	#getters
	def getSize(self):
		return len(self.__members)

	def getMemberByIndex(self, i):
		if not isinstance(i,int):
			return None
		
		return self.__members[i]

	def getMemberList(self):
		return self.__members

	def getMinSize(self):
		return self.__minsize

	def getMaxSize(self):
		return self.__maxsize

	def getRating(self):
		return self.__rating
	#end getters

	#setters		
	def setMinSize(self, i):
		if not isinstance(i,int):
			return
		else:
			self.__minsize = i

	def setMaxSize(self, i):
		if not isinstance(i,int):
			return
		else:
			self.__maxsize = i

	def setRating(self, i):
		if not isinstance(i, float):
			return
		
		if i < 0 or i > 1.0:
			return
		else:
			self.__rating = i	

	def setMemberList(self, m_list):
		if not isinstance(m_list, list):
			return
		self.__members = m_list

	#end setters
			
	def deepCopy(self, other):
		if not isinstance(other, Team):
			return

		for member in other.getMemberList():
			self.__members.append(member)
		self.setMinSize(other.getMinSize())
		self.setMaxSize(other.getMaxSize())
		self.setRating(other.getRating())

	#returns current number of team members
	def getTeamSize(self):
		return len(self.__members)

	#adds a Student to the team, only allows Student objects
	#if student is found in the list it is not added. returns
	#true or false depending on successful insert.
	def insertStudent(self, s):
		if len(self.__members) >= self.getMaxSize():
			return False

		if type(s).__name__ != "Student":
			return False

		for member in self.__members:
			if s == member:
				return False 


		self.__members.append(s)
		return True

	#removes a student from the team. returns true
	#if action was successful, false otherwise.
	def remStudent(self, s):
		if type(s).__name__ != "Student":
			return False

		for i in range(len(self.__members)):
			if s == self.__members[i]:
				del self.__members[i]
				return True

		return False

	#purges the list of members on this team. also affects
	#anything that references to this value. (exampel:
	#cpy = self.__members; cpy will be purged too)
	def purgeMembers(self):
		del self.__members[:]

	#determines if two teams are equivalent
	def __eq__(self,other):
		if self.getTeamSize() != other.getTeamSize():
			return False

		for i in range(len(self.__members)):
			if self.__members[i] != other.__members[i]:
				return False
		return True

	#represents the team object as a string
	def __str__(self):
		output = ""
		for i in range(len(self.__members)):
			output += str(self.__members[i]) + "\n"

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

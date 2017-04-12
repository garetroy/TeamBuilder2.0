##
#
# Written by Jared Paeschke, jpaeschk@uoregon.edu
# Course: CIS 422 Spring 2017
#
# This class is part of a team project to make a team formation automater &
# optimizer. Project members include Alister Maguire, Jared Paeschke, & 
# Garett Roberts.
# 
##

from student import Student
from day import Day

class Team:

	#constructor
	def __init__(self, minimum, maximum):
		self.members = []
		self.minsize = minimum
		self.maxsize = maximum
		self.teamrating = 0

	#returns current number of team members
	def getTeamSize():
		return len(self.members)

	#adds a Student to the team, only allows Student objects
	#if student is found in the list it is not added. returns
	#true or false depending on successful insert.
	def insertStudent(self, student):
		if type(student).__name__ != "Student":
			return False

		for i in range(len(self.members)):
			if student == self.members[i]:
				return False

		self.members.append(student)
		return True

	#determines if two teams are equivalent
	def __eq__(self,other):
		if self.getTeamSize() != other.getTeamSize():
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

		return output

#tester function the Team class, only runs when this module is main
def test_team():
	d1 = Day("Tuesday")
	d1.insertTime(10)
	d1.insertTime(13)

	d2 = Day("Wednesday")
	d2.insertTime(10)
	d2.insertTime(14)

	s1 = Student("Jared Paeschke","mahananaka@gmail.com")
	s1.insertDay(d1)
	s1.insertDay(d2)

	s2 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
	s2.insertDay(d2)

	t = Team(3,4)
	print("t.insertStudent(s1): " + str(t.insertStudent(s1)))
	print("t.insertStudent(s1): " + str(t.insertStudent(s1)))
	print("t.insertStudent(s2): " + str(t.insertStudent(s2)))

	print(t)

if __name__ == "__main__":
	test_team()

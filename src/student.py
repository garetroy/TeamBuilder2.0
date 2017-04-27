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
# Alister Maguire, Fri Apr 14 16:06:16 PDT 2017
# Added teammate preferences and methods associated 
# with adding and removing them. 
#
# Alister Maguire, Sun Apr 16 15:13:48 PDT 2017
# commented out areas of str method that used no 
# longer defined class members. 
#
# Garett Roberts, Sun Apr 16 17:41:00 PDT 2017
# Added self parameter of memberfunction getPrefs
##

from day import Day

class Student:

	#constructor
	def __init__(self,pname,pemail):
		self.__name = pname
		self.__email = pemail
		self.__filters = {}
		#self.__days = []
		#self.__langprefs = []
		#self.__teammateprefs = []

	#start getters
	def getName(self):
		return self.__name

	def getEmail(self):
		return self.__email

	def getPrefs(self):
		return self.__filters

	#end getters

	#start setters
	def setName(self, n):
		if not isinstance(n,str):
			return False
		else:
			self.__name = n
			return True

	def setEmail(self,e):
		if not isinstance(n,str):
			return False
		else:
			self.__name = e
			return True

	def setFilters(self,f):
		if not isinstance(f,dict):
			return False
		else:
			self.__filters = f
			return True
	#end setters

	#compares two instances of Student based on their email address
	#this returns true when both have the same email
	def __eq__(self,other):
		if (self.__email != other.__email) or (self.__name != other.__name) or (self.__filters != other.__filters):
			return False

		return True

	#outputs values of Student class
	def __str__(self):
		output = self.__name + " " + self.__email
		#for i in range(len(self.__days)):
		#	output += " " + str(self.__days[i])
		#
		#for i in range(len(self.__langprefs)):
		#	output += " " + self.__langprefs[i]

		return output


#tests the class, only runs when this module is main
def test_student():
	s = Student("Jared Paeschke","mahananaka@gmail.com")

	s2 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
	print("s==s: " + str(s == s2))
	print("s==s: " + str(s == s))


if __name__ == "__main__":
	test_student()

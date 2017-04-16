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

	def getPrefs():
		return self.__filters

	'''
	def getDays(self):
		return self.__days

	def getLangPrefs(self):
		return self.__langprefs
	'''
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

	'''
	#associates a day with a student, won't allow days with the same name
	#prevents things that are not a 'Day' type from being added. Returns
	#true or false if insert is successful
	def insertDay(self, day):
		if type(day).__name__ != "Day":
			return False

		for i in range(len(self.__days)):
			if day == self.__days[i]:
				return False

		self.__days.append(day)
		return True

	#removes day from the list of days associated with this student if
	#day equals a day in the list
	def remDay(self, day):
		if type(day).__name__ != "Day":
			return False

		for i in range(len(self.__days)):
			if day == self.__days[i]:
				del self.__days[i]
				return True

		return False

	#purges the list of days associated with this student, this will also 
	#clear anything that references self.__days as well (i.e. cpy = self.__days
	#cpy will be cleared as well)
	def purgeDays(self):
		del self.__days[:]

        #Insert a prefered teammate to the prefered teammates list. 
        #The teammate will only be added if they are not already in the
        #list. If the add is a succes, True is returned. Otherwise, False. 
	def insertTeammatePref(self,other):
		if not isinstance(other, str):
			return False

		if other in self.__teammateprefs:
			return False            

		self.__teammateprefs.append(other)
		return True
        
        #Remove a teammate preference. Returns True if succesful, 
        #false otherwise. 
	def remTeammatePref(self,other):
		if not isinstance(other, str):
			return False

		if other in self.__teammateprefs:
			self.__teammateprefs.remove(other)
			return True            

		return False

        #Reset the teammate preferences to an empty list
	def purgeTeammatePrefs(self):
		self.__teammateprefs = []

	#associates a language with a students preferences, must pass a string
	#if the string is already in the list it will not add it. Returns true
	#or false if insert is successful
	def insertLangPref(self,lang):
		if not isinstance(lang,str):
			return False

		for i in range(len(self.__langprefs)):
			if lang == self.__langprefs[i]:
				return False

		self.__langprefs.append(lang)
		return True

	#removes a langue preference from the student. Only accepts
	#a string and returns true removal occurs, otherwise false
	def remLangPref(self, lang):
		if not isinstance(lang,str):
			return False

		for i in range(len(self.__langprefs)):
			if lang == self.__langprefs[i]:
				del self.__langprefs[i]
				return True
		return False

	#purges the list of language preferences associated with this student, 
	#this will also clear anything that references self.__langprefs as well.
	#(i.e. cpy = self.__langprefs; cpy will be cleared as well)
	def purgeLangPrefs(self):
		del self.__langprefs[:]
	'''

	#compares two instances of Student based on their email address
	#this returns true when both have the same email
	def __eq__(self,other):
		if self.__email != other.__email:
			return False

		return True

	#outputs values of Student class
	def __str__(self):
		output = self.__name + " " + self.__email
		#for i in range(len(self.__days)):
		#	output += " " + str(self.__days[i])
		
		#for i in range(len(self.__langprefs)):
		#	output += " " + self.__langprefs[i]

		return output
		

#tests the class, only runs when this module is main
def test_student():
	s = Student("Jared Paeschke","mahananaka@gmail.com")

	s2 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
	print("s==s: " + str(s == s2))
	print("s==s: " + str(s == s))


	print('student: ' + str(s))


	print('student: ' + str(s))


if __name__ == "__main__":
	test_student()

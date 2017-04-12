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

from day import Day

class Student:

	#constructor
	def __init__(self,pname,pemail):
		self.name = pname
		self.email = pemail
		self.days = []
		self.langprefs = []

	#associates a day with a student, won't allow days with the same name
	#prevents things that are not a 'Day' type from being added. Returns
	#true or false if insert is successful
	def insertDay(self, day):
		if type(day).__name__ != "Day":
			return False

		for i in range(len(self.days)):
			if day.name == self.days[i].name:
				return False

		self.days.append(day)
		return True

	#associates a language with a students preferences, must pass a string
	#if the string is already in the list it will not add it. Returns true
	#or false if insert is successful
	def insertLangPref(self,lang):
		if not isinstance(lang,str):
			return False;

		for i in range(len(self.langprefs)):
			if lang == self.langprefs[i]:
				return False

		self.langprefs.append(lang)
		return True

	#compares two instances of Student based of their email address
	def __eq__(self,other):
		if self.email != other.email:
			return False

		return True

	#outputs values of Student class
	def __str__(self):
		output = self.name + " " + self.email
		for i in range(len(self.days)):
			output += " " + str(self.days[i])
		
		for i in range(len(self.langprefs)):
			output += " " + self.langprefs[i]

		return output
		

#tests the class, only runs when this module is main
def test_student():
	d1 = Day("Tuesday")
	d1.insertTime(10)
	d1.insertTime(13)

	d2 = Day("Wednesday")
	d2.insertTime(10)
	d2.insertTime(14)

	s = Student("Jared Paeschke","mahananaka@gmail.com")
	print("s.insert(int): " + str(s.insertDay(10)))
	print("s.insert(d1): " + str(s.insertDay(d1)))
	print("s.insert(d2): " + str(s.insertDay(d2)))
	print("s.insert(d2): " + str(s.insertDay(d2)))

	s2 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
	print("s==s: " + str(s == s2))
	print("s==s: " + str(s == s))

	print("s.insertLangPref(str1): " + str(s.insertLangPref("C++")))
	print("s.insertLangPref(int): " + str(s.insertLangPref(10)))
	print("s.insertLangPref(str1): " + str(s.insertLangPref("C++")))
	print("s.insertLangPref(str2): " + str(s.insertLangPref("Java")))


if __name__ == "__main__":
	test_student()

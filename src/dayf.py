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
from tfilter import Filter

class Day(Filter):

	#constructor
	def __init__(self, d):
		self.__name = d
		self.__times = []

	#start getters
	def getName(self):
		return self.__name

	def getTimes(self):
		return self.__times
	#end getters

	#start setters
	def setName(self,n):
		if not isinstance(n,str):
			return

		self.__name = n
	#end setters

	#inserts a time(int) into the Day, only allows [0-23] and
	#doesn't allow duplicates.
	def insertTime(self, t):
		if not isinstance(t,int):
			return False

		if(t < 0 or t > 23):
			return False

		for i in range(len(self.__times)):
			if t == self.__times[i]:
				return False
		else:
			self.__times.append(t)
			return True

	#removes a time if found within the list of times. Also
	#returns true if successful; false otherwise.
	def removeTime(self, t):
		if not isinstance(t,int):
			return False

		for i in range(len(self.__times)):
			if t == self.__times[i]:
				del self.__times[i]
				return True

		return False
	
	#purges the times associated with this day. affects anything
	#that references to times. (i.e. cpy = self.__times; cpy is
	#also purged as well).
	def purgeTimes(self):
		del self.__times[:]

	#no implementation as of yet
	def __gt__(self,other):
		return False
		
	#no implementation as of yet
	def __ls__(self,other):
		return False

	#exames two Day objects and determines if they are equivalent
	def __eq__(self,other):
		if self.__name != other.__name:
			return False
		else:
			if len(self.__times) != len(other.__times):
				return False

			for i in range(len(self.__times)):
				if self.__times[i] != other.__times[i]:
					return False
		
		return True

	#outputs the name of the day and the times addes to that day
	def __str__(self):
		output = self.__name + " "
		for i in range(len(self.__times)):
			output += str(self.__times[i]) + ","

		return output[:-1]

#tester function of the Day class, only runs when this module is main
def test_day():
	w = Day("Monday")
	x = Day("Tuesday")
	x.insertTime(10)
	x.insertTime(14)
	x.insertTime(18)
	print(x.insertTime(10))
	print(x.insertTime(-1))
	print(x.insertTime(24))
	print(x)

	y = Day("Tuesday")
	y.insertTime(10)
	y.insertTime(14)
	y.insertTime(18)

	z = Day("Tuesday")
	z.insertTime(10)
	z.insertTime(14)
	z.insertTime(15)

	print(str(x == y))
	y.insertTime(11)
	print(str(x == y))
	print(str(x == z))
	print(str(x == w))



if __name__ == "__main__":
	test_day()

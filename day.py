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


class Day:

	#constructor
	def __init__(self, d):
		self.name = d
		self.times = []

	#inserts a time(int) into the Day, only allows [0-23]
	def insertTime(self, t):
		if(t < 0 or t > 23):
			return False
		else:
			self.times.append(t)
			return True

	#no implementation as of yet
	def __gt__(self,other):
		return False
		
	#no implementation as of yet
	def __ls__(self,other):
		return False

	#exames two Day objects and determines if they are equivalent
	def __eq__(self,other):
		if self.name != other.name:
			return False
		else:
			if len(self.times) != len(other.times):
				return False

			for i in range(len(self.times)):
				mine = self.times[i]
				theirs = other.times[i]
				if mine != theirs:
					return False
		
		return True

	#outputs the name of the day and the times addes to that day
	def __str__(self):
		output = self.name + " "
		for i in range(len(self.times)):
			output += str(self.times[i]) + ","

		return output[:-1]

#tester function of the Day class, only runs when this module is main
def test_day():
	w = Day("Monday")
	x = Day("Tuesday")
	x.insertTime(10)
	x.insertTime(14)
	x.insertTime(18)
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

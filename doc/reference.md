## Classes Overview
* Team
* Student
* Day
* IOManager
* AlgorithmManager

### Team:
Contains multiple students to form a single team.

Dependencies:
* Student
* Day

Members:
* members - list
* minsize - int
* maxsize - int
* rating - float

Functions:
* \_\_init\_\_(int,int)
* \_\_eq\_\_(team)
* \_\_str\_\_()
* getTeamSize()
* insertStudent(student)
* remStudent(student)
* purgeMembers()
        
Team.\_\_init\_\_(self,minimum,maximum)

>Description:
>>Creates an instance of team with minimum and maximum set. Also
>>initializes the team members to an empty list.

>Parameters:
>>minimum - int that will be the min team size
>>maximum - int that will be the max team size

>Returns:
>>an instance of Team

## Classes Overview
    Team
    Student
    Day
    IOManager
    AlgorithmManager

### Team:
    Contains multiple students to form a single team.

    Dependencies:
        Student
        Day

    Members:
        members - list
        minsize - int
        maxsize - int
        rating - float

    Functions:
        __init__(int,int)
        __eq__(team)
        __str__()
        getTeamSize()
        insertStudent(student)
        remStudent(student)
        purgeMembers()
        
    Team.__init__(self,minimum,maximum)

        Description:
        Creates an instance of team with minimum and maximum set. Also
        initializes the team members to an empty list.

        Parameters:
        minimum - int that will be the min team size
        maximum - int that will be the max team size

        Returns:
        an instance of Team

# Classes Overview
* [Team](#team)
* [Student](#student)
* [Day](#day)
* [IOManager](#iomanager)
* [AlgorithmManager](#algorithmmanager)

## Team
Contains multiple students to form a single team.

| Dependencies | Members | Functions | 
|---|---|---|
| Student | members - list | \_\_init\_\_(int,int) |      
| Day. | minsize - int  | \_\_eq\_\_(team) |
| | maxsize - int  | \_\_str\_\_() |
| | rating - float | getTeamSize() |
| | | insertStudent(student) |
| | | remStudent(student) |
| | | purgeMembers() |

        
Team.\_\_init\_\_(self,minimum,maximum)
    
    -- Description --
    Creates an instance of team with minimum and maximum set. Also
    initializes the team members to an empty list.

    -- Parameters --
    minimum - int that will be the min team size
    maximum - int that will be the max team size

    -- Returns --
    an instance of Team

## Student

## Day

## IOManager

## AlgorithmManager

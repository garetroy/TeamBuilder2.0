# Overview
1. [Classes](#classes)
2. [Functions](#functions)

## Classes
* [Team](#team)
* [Student](#student)
* [Day](#day)
* [IOManager](#iomanager)
* [AlgorithmManager](#algorithmmanager)

### Team
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

        
**Team.\_\_init\_\_(self,minimum,maximum)**
    
    -- Description --
    Creates an instance of team with minimum and maximum set. Also
    initializes the team members to an empty list.

    -- Parameters --
    minimum - int that will be the min team size
    maximum - int that will be the max team size

    -- Returns --
    an instance of Team

**Team.\_\_eq\_\_(self,other**
    
    -- Description --
    Returns true when self and other are equal

    -- Parameters --
    other - a team to compare with

    -- Returns --
    a boolean

**Team.\_\_str\_\_(self)**

    -- Description --
    Returns a string that represents the team

    -- Parameters --
    N/A

    -- Returns --
    a string

**Team.getTeamSize(self)**

    -- Description --
    Returns the current size of the team

    -- Parameters --
    N/A

    -- Returns --
    an int

**Team.insertStudent(self,s)**

    -- Description --
    Inserts a student into the team object if it doesn't exceed the max team size.
    Returns a weather the insertion was successful or not.

    -- Parameters --
    s - the student object to insert
 
    -- Returns --
    a boolean

**Team.remStudent(self,s)**

    -- Description --
    Removes Student s from the team if it is found. Only returns true when s is
    found and removed.

    -- Parameters --
    s - the Student to be removed

    -- Returns --
    a boolean

**Team.purgeMembers(self)**

    -- Description --
    Empties the entire list of  team members.

    -- Parameters --
    N/A

    -- Returns --
    N/A

### Student
Contains the information of a single student.

| Dependencies | Members | Functions |
|---|---|---|
| Day | name - string | \_\_init\_\_(str,str) |      
| | email - string | \_\_eq\_\_(student) |
| | filters - dict | \_\_str\_\_() |

**Student.\_\_init\_\_(self,name,email)**

    -- Description --
    Creates an instance of a Student object with the name and email values set to 
    the ones past in the constructor.

    -- Parameters --
    name - the students name as a string
    email - the students email as a string

    -- Returns --
    a Student object

**Student.\_\_eq\_\_(self,other)**

    -- Description --
    Compare to Student other and determine if they are the same student. Returns
    true when they have the same email address.
     
    -- Parameters --
    other - the student to compare with
 
    -- Returns --
    a boolean

**Student.\_\_str\_\_(self)**

    -- Description --
    Returns a string that represents the student object.
    
    -- Parameters --
    N/A
 
    -- Returns -- 
    a string

### Day
Holds information for available times for a single day.

| Dependencies | Members | Functions |
|---|---|---|
| N/A | name - string | \_\_init\_\_(str,str) |      
| | times - string | \_\_eq\_\_(student) |
| | | \_\_str\_\_() |
| | | insertTime(int) |
| | | remTime(int) |
| | | purgeTime() |

**Day.\_\_init\_\_(self,d)**

    -- Description --
    Creates an instance of day object with the day set to d

    -- Parameters --
    d - a day of the week as a string, i.e. "Monday"

    -- Returns --
    a Day object

**Day.\_\_eq\_\_(self,other)**

    -- Description --
    Compares against Day other and determines if they are the same day.
    Returns true when they are the same day.
    
    -- Parameters --
    other - a Day to compare against

    -- Returns --
    a boolean

**Day.\_\_str\_\_(self)**

    -- Description --
    Returns a string that represents the Day object.
    
    -- Parameters --
    N/A

    -- Returns --
    a string

**Day.insertTime(self,t)**

    -- Description --
    Add t to the day if a valid; t is invalid when not an integer, not in [0,23] or
    if it is already associated with this Day. Returns true if t is inserted.
    
    -- Parameters --
    t - an int representing an hour of the day.

    -- Returns --
    a boolean

**Day.removeTime(self, t)**

    -- Description --
    Removes t from this Day if it is found. Returns true if found and removed.
    
    -- Parameters --
    t - an int representing the hour to be removed

    -- Returns --
    a boolean

**Day.purgeTime(self)**

    -- Description --
    Empties the times list for this Day.
    
    -- Parameters --
    N/A

    -- Returns --
    N/A

### IOManager
Handles I/O of data from file to Student and Day data structures and vice versa.

| Dependencies | Members | Functions |
|---|---|---|
| Day | N/A | \_\_init\_\_(c_data,roster) |      
| Student | | read(str) |
| difflib | | write(str, team[]) |
| csv | | blockParser(str) | 
| sys | | nameChecker(str) |

**IOManager.\_\_init\_\_(self)**

    -- Description --
    Initialize the manager with an in a config and a roster.

    -- Parameters --
    c_data - configuration dict with readers and writers.
    roster - a list of valid student names in the format ["last_name, first_name", ...]
    
    -- Returns --
    an instance of IOManager

**IOManager.read(self, path)**

    -- Description --
    Returns the appropriate reader function to read in a file for data collection.

    -- Parameters --
    path - the path to the input file as a string

    -- Returns --
    a function

**IOManager.write(self, path, teams)**

    -- Description --
    Returns the appropriate writer function to write data to output.

    -- Parameters --
    path - the path to the output file

    -- Returns --
    a function

**IOManager.blockParser(self, block)**

    -- Description --
    Parses a contiguous block of csv data. These blocks occur when  there
    are multiple elements in a single column and are often seperated by
    semicolons. The data is broken into chunks and returned as a list.

    -- Parameters --
    block - a block of csv data as a string

    -- Returns --
    a string[]

**IOManager.nameChecker(self, name)**

    -- Description --
    Checks to see if a name is valid. A name is considered valid if a single
    from the following is met:
    a. The full name is on the roster
    b. the first name is on the roster
    c. the full name is a 90% match to a name on the roster (spelling errors)
    
    Returns a tuple that the first element is a boolean representing success
    and the second element is the match.

    -- Parameters --
    name - a student name as a string

    -- Returns --
    a (bool,string)

### AlgorithmManager

| Dependencies | Members | Functions |
| --- | --- | --- |
| Team | k - int | \_\_init\_\_(int, int ,int, int)  |
| Student | d - int | getFilterDictionary() |
| SwapList | n - int | setFilterDictionary(dict) |
| filters - * | | addFilter(dict) |
| random - randrange | | initTeamSet(Student[]) |
| os | | weightCalc(team) |
| sys | | getWeight(Student, Student) |
| | | swapMembers(Team[]) |
| | | deviation(Team[]) |
| | | runMain(Student[]) |

**AlgorithmManager.\_\_init\_\_(self, team_size, k, d, n)**

    -- Description --
    Creates an instance of AlgorithmManager with the passed parameters.

    -- Parameters --
    team_size - the team size as an int
    k - an int that sets how many sets of base teams are created. Defaults to 10.
    d - an int that sets how many times we create the base teams set. Defaults to 20.
    n - an int that sets how many swaps to do. Defaults to 25.
    
    -- Returns --
    a AlgorithmManager object

**AlgorithmManager.getFilterDictionary(self)**

    -- Description --
    Returns the filter dictionary which links preferences to the functions that parse
    them.

    -- Parameters --
    N/A

    -- Returns --
    a dict

**AlgorithmManager.setFilterDictionary(self,fd)**

    -- Description --
    Overwrites the filter dict with a new one.

    -- Parameters --
    fd - a dict of filters

    -- Returns --
    N/A

**AlgorithmManager.addFilter(self, filterin)**

    -- Description --
    Appends a filter into the filters dict

    -- Parameters --
    filterin - a dict representing the new filters

    -- Returns --
    N/A

**AlgorithmManager.initTeamSet(self, students)**

    -- Description --
    Creates a list of Team objects where each Student in the list of students
    is added to one team. Each team is randomly created because they will be
    improved upon later.

    -- Parameters --
    students - a list of Student objects

    -- Returns --
    a Team[]

**AlgorithmManager.weightCalc(self, team_in)**

    -- Description --
    Calculates a weighted rating for how ideal a team is. The rating field of
    team_in is updated to reflect this calculation.

    -- Parameters --
    team_in - a team to be rated, this is modified by this function

    -- Returns --
    N/A

**AlgorithmManager.getWeight(self, studnet1, student2)**

    -- Description --
    Compares student1 and student2 to each other determining how good of a match
    they are with each other. The result calculated is a weighted double and is
    returned. Result is commutative, so it does not matter which student is
    first or second. Returns a rational number between 0 and 1.

    -- Parameters --
    student1 - a student object, one half of the calculation
    student2 - a student object, the other half of the calculation.
   
    -- Returns --
    a float

**AlgorithmManager.swapMembers(self,teams)**

    -- Description --
    Swaps around the team members of several Team objects. After the swap it 
    returns the list of newly made Team objects.

    -- Parameters --
    teams - a list of Team objects

    -- Returns --
    a Team[]

**AlgorithmManager.deviation(self,teams)**

    -- Description --
    Calculates the difference between the min and max rated teams.
 
    -- Parameters --
    teams - a list of Team objects
    
    -- Returns --
    a float

**AlgorithmManager.runMain(self,students)**

    -- Description --
    Using students, a list of all students, this is the main logic that determines
    team assignments. Attempts to balance team ratings.
    
    -- Parameters --
    students - a list of Student objects
    
    -- Returns --
    a Team[]

## Functions
* [filters](#filters)
* [io_functions](#io_functions)

### filters

| Dependencies | Functions|
| --- | --- |
| Student | scheduleFilter(Student,Student) |
| os | languageFilter(Student,Student) |
| sys | teammateFilter(Student,Student) |

**scheduleFilter(s1,s2)**

    -- Description --
    Rates how good a match two students are based on their schedules. The
    rating returned is a rational number between 0 and 1.

    -- Parameters --
    s1 - the student to be compared with s2
    s2 - the student to be compared with s1
    
    -- Returns --
    a float

**languageFilter(s1,s2)**

    -- Description --
    Rates how good a match two students are based on their programming
    language preferences. The rating returned is a rational number 
    between 0 and 1.

    -- Parameters --
    s1 - the student to be compared with s2
    s2 - the student to be compared with s1
    
    -- Returns --
    a float

**teammateFilter(s1,s2)**

    -- Description --
    Rates how good a match two students are based on their desired teammates.
    The rating returned is a rational number between 0 and 1.

    -- Parameters --
    s1 - the student to be compared with s2
    s2 - the student to be compared with s1
    
    -- Returns --
    a float

### io_functions

| Dependencies | Functions|
| --- | --- |
| Student | cvsReader(IOManager, str) |
| Day | txtWriter(IOManager, str, Team[]) |
| IOManager | scoreWriter(IOManager, str, Team[] |
| csv | |
| os | |
| sys | |

**csvReader(iomanager, path)**

    -- Description --
    Read data from a csv file and create Student objects from this data. The
    format of the csv file is currently something that must be static.
    Current expected layout of csv file:
    >Timestamp, name, email, mon, tues, wed, thurs, fri, sat, sun, lang, mate1, mate2

    Maybe this can become more dynamic.

    -- Parameters --
    path - the path to the target csv file.

    -- Returns --
    a Student[]

**txtWriter(iomanager,path,teams)**

    -- Descriptioin -- 
    This writes the team, its score, and the member's names and email addresses
    to the file specified by path.

    -- Parameters --
    path - the path of the file to be written to.
    teams - a list of teams to be written to file.

    -- Return --
    N/A

**scoreWriter(iomanager,path,teams)**

    -- Description --
    This is primarily used for testing and debugging. It prints the scores of
    each team to the file that path points to.

    -- Parameters --
    path - the path of the file to be written to
    teams - a list of teams to be written to file
    
    -- Return --
    N/A

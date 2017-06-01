# Overview
1. [Classes](#classes)
2. [Functions](#functions)

## Classes
* [Team](#team)
* [Student](#student)
* [Day](#day)
* [IOManager](#iomanager)
* [AlgorithmManager](#algorithmmanager)
* [ConfigData](#configdata)
* [GuiInterface](#guiinterface)
* [SwapList](#swaplist)
* [Root](#root) - GUI root
* [TheadedTask](#threadedtask)

### Team
Contains multiple students to form a single team.

| Dependencies | Members | Functions | 
|---|---|---|
| Student | members - list | \_\_init\_\_(int,int) |      
| Day. | minsize - int  | \_\_eq\_\_(team) |
| SwapList | maxsize - int  | \_\_str\_\_() |
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
| ConfigData | c_data - ConfigData   | \_\_init\_\_(c_data,roster) |      
| sys | | read(str) |
| csv | | write(str, team[]) |
| difflib | | blockParser(str) | 
| | | nameChecker(str) |

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
Handles the different parts of running the algorithm for forming teams.

| Dependencies | Members | Functions |
| --- | --- | --- |
| Team | __team_size - int | \_\_init\_\_(int, int ,int, int)  |
| Student | k - int | getFilterDictionary() |
| SwapList | d - int | setFilterDictionary(dict) |
| filters | n - int | addFilter(dict) |
| random | | initTeamSet(Student[]) |
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

### ConfigData
An object that gathers data from the config.json and holds the settings used
for TeamBuilder2.0

| Dependencies | Members | Functions |
| --- | --- | --- |
| io_functions | filter_dictionary - dict | \_\_init\_\_() |
| filters | readers - dict | |
| json | writers - dict | |
| pathlib | email - dict | |
| os | defaults - dict | |
| sys | | |

**ConfigData.\_\_init\_\_()**

    -- Description --
    Reads the settings from the ./config/config.json file and creates an object
    with all the settings stored within it. Each member of the class is 
    populated with the setting specific to its section.

    -- Parameters --
    N/A

    -- Return --
    a ConfigData object

### GuiInterface
This separates the GUI and the algorithmn to increase independece of each other

| Dependencies | Members | Functions |
| --- | --- | --- |
| Day | teams - Team[] | \_\_init\_\_() |
| Student | roster - str[] | loadRoster(str) |
| Team | c_data - ConfigData | startManager() |
| IOManager | manager - IOManager | readCsv |
| ConfigData | students - Student[] | startAlgorithm(int) |
| AlgorithManager | algorithm - AlgorithmManager | runGeneral(str,str,int) |
| inform | outputpath - str | setOutputPath(str) |
| pathlib | email - str | writeFile() |
| | password - str | reShuffleAll() |
| | saved - boolean | reShuffleTeams() |
| | | reShuffleSelectedTeams(int[]) |
| | | sendEmail(team[],str,str,boolean) |

**GuiInterface.\_\_init\_\_(self)**

    -- Description --
    Creates an instance of the GuiInterface object with all members set to nothing.

    -- Parameters --
    N/A

    -- Return --
    a GuiInterface object

**GuiInterface.loadRoster(self,rostertext)**

    -- Description --
    Loads the roster text file into the self.roster

    -- Parameters --
    rostertext - the filepath of the roster file

    -- Return --
    N/A

**GuiInterface.startManager(self)**

    -- Description --
    Starts the IOManager by loading it and the config into self.c_data and self.manager

    -- Parameters --
    N/A

    -- Return --
    N/A

**GuiInterface.readCsv(self,intext)**

    -- Description --
    Reads the csv file using the IOManager into self.students

    -- Parameters --
    intext - the csv file to be read in

    -- Return --
    N/A

**GuiInterface.startAlgorithm(self)**

    -- Description --
    Loads the AlgorithmManager into self.algorithm with team size set to teamsize.
    Then populates the self.teams with the created teams.

    -- Parameters --
    teamsize - the desired team sizes as an int

    -- Return --
    N/A

**GuiInterface.runGeneral(self,rostertext,intext,teamsize)**

    -- Description --
    Runs loadRoster(), startManager(), readCsv(), and startAlgorithm() in one
    wrapping function.

    -- Parameters --
    rostertext - the roster file passed. This is passed to loadRoster()
    intext - the csv data file. This is passed to readCsv()
    teamsize - the desired team sizes - This is passed to startAlgorithmn()

    -- Return --
    N/A

**GuiInterface.setOutputPath(self,outputpath)**

    -- Description --
    Sets self.outputpath, which will be used by writeFile().

    -- Parameters --
    outputpath - the file path to write to as string

    -- Return --
    N/A

**GuiInterface.writeFile(self)**

    -- Description --
    Writes the file to self.outputpath using the IOManger located in self.manager
    If the file exists, it will append an increasing int to the end of the file name.
    
    -- Parameters --
    N/A

    -- Return --
    N/A

**GuiInterface.reShuffleAll**

    -- Description --
    Completely reruns the algorithm, if a prior team list exists it is overwritten.
    
    -- Parameters --
    N/A

    -- Return --
    N/A

**GuiInterface.reShuffleTeams(self)**

    -- Description --
    Shuffles the teams using the swapMember function from the AlgorithmManager.

    -- Parameters --
    N/A

    -- Return --
    N/A

**GuiInterface.reShuffleSelectedTeams(self,indexes)**

    -- Description --
    Shuffles the members of the selected teams around.

    -- Parameters --
    indexes - a list of int representing the teams to shuffle

    -- Return --
    N/A

### SwapList
An improved list for removing the middle elements.

| Dependencies | Members | Functions |
| --- | --- | --- |
| | | swapPop(self, idx) |

**SwapList.swapPop(self, idx)**

    -- Description --
    Swaps the last element and the element at index idx and then pops the end
    of the list off.

    -- Parameters --
    idx - an int in the range of 0 and elements-1.
    
    -- Returns --
    the element of the list at position idx.
    
### Root
Creates the root tkinter GUI.

| Dependencies | Members | Functions |
| --- | --- | --- |
| os | queue - Queue | \_\_init\_\_(Tk,str,str) |
| time | parent - Tk | centerWindow(Tk) | 
| threading | interface - GuiInterface | startWindow() |
| argparse | loadWindow | resetWindow() |
| tkinter | remember - boolean | startMainUI() |
| | initialized - boolean | optionUI() |
| | csvpath - str | inspectTeamUI() |
| | rosterpathh - str | memberSwapUI() |
| | outpathh - str | emailScreen() |
| | teamsizeh - str | emailTeams() |
| | | loadingScreen() |
| | | memberSwap() |
| | | switchTeams(int[]) |
| | | swapSizeCheck(int[] |
| | | shuffleSelected() |
| | | reRun() |
| | | submitFiles() |
| | | checkThread() |
| | | testNumber() |
| | | csvstartfilebrowser() |
| | | rosterstartfilebrowser() |
| | | outputstartfilebrowser() |

**Root.\_\_init\_\_(self,parent,csvpath,rosterpath)**

    -- Description --
    Initializes the root tkinter window and other members.

    -- Parameters --
    parent - the root Tk object
    csvpath - filepath to csv data file, as a string, defaults to empty string
    rosterpath - filepath to roster, as a string, defaults to empty string

    -- Returns --
    N/A

**Root.centerWindow(self,notself=None)**

    -- Description --
    Centers the main window or the one passed if given an argument.

    -- Parameters --
    noself - Tk object, which will be centered. Defaults to None
    
    -- Returns --
    N/A

**Root.startWindow(self)**

    -- Description --
    Starts and creates the window for the UI.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.resetWindow(self)**

    -- Description --
    Resets the window by destroying the old if it exists and running startWindow() again.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.startMainUI(self)**

    -- Description --
    Creates and positions all objects on the main window and links them with their handlers.
    This handles most of the heavy work for the GUI.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.optionUI(self)**

    -- Description --
    Creates the window that displays the generated teams.
    
    -- Parameters --
    N/A

    -- Returns -- 
    N/A

**Root.inspectTeamUI(self)**

    -- Description --
    Creates the window that allows the display of team information

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.memberSwapUI(self)**

    -- Description --
    Creates the window that allows member swapping.

    -- Parameters --
    indexes - list of indices that point to which teams to swapp.

    -- Returns --
    N/A

**Root.emailScreen(self)**

    -- Description --
    Creates the email authentication screen for sending emails

    -- Parameters --
    N/A

    -- Returns -- 
    N/A

**Root.emailTeams(self)**

    -- Description --
    Wrapper which does the calling of sending out emails

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.loadingScreen(self)**

    -- Description --
    Starts loading screen and disables buttons so no other actions can
    be taken while calculations are ran.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.memberSwap(self)**

    -- Description --
    Validates selections so that memberSwapUI() receives valid arguments.

    -- Parameters --
    N/A

    -- Returns -- 
    N/A

**Root.switchTeams(self)**

    -- Description --
    Swaps selected team members from one team to another.

    -- Parameters --
    indexes - list of int repesenting the appropriate team member.

    -- Returns --
    N/A

**Root.swapSizeCheck(self)**

    -- Description --
    Checks that when you finish swapping team members the teams are still valid sizes.

    -- Parameters --
    indexes - a list of integers to the teams to check

    -- Returns --
    N/A

**Root.shuffleSelected(self)**

    -- Description --
    Wrapper function that shuffles the selected teams.

    -- Parameters --
    N/A

    -- Returns -- 
    N/A

**Root.reRun(self)**

    -- Description --
    Wrapper functioin that reruns the algorithm.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.submitFiles(self)**

    -- Description --
    Validates the inputs to the main algorithm and then runs the core
    of the TeamBuilder2.0 program.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.checkThread(self, thread, function)**

    -- Description --
    Checks to see if the given thread is dead, once it is it calls the
    specified handler function.

    -- Parameters --
    thread - the ThreadedTask object to check.
    function - the handler which is called.

    -- Returns -- 
    N/A

**Root.testNumber(self,i,minimum=0,maximum=5)**

    -- Description --
    Checks if i is in in the range of minimum and maximum (inclusive). Returns
    True or False.

    -- Parameters --
    i - number to check
    minimum - lower bound range, defaults to 0
    maximum - upper bound range, defaults to 5

    -- Returns --
    a boolean

**Root.csvstartfilebrowser(self)**

    -- Description --
    Starts the filebrowser for the csv file.

    -- Parameters --
    N/A

    -- Returns --
    N/A

**Root.rosterstartfilebrowser(self)**

    -- Description --
    Starts the filebrowser for the roster file.

    -- Parameters --
    N/A

    -- Returns -- 
    N/A

**Root.outputstartfilebrowser(self)**

    -- Description --
    Starts the filebrowser to select an output file.

    -- Parameters --
    N/A

    -- Returns --
    N/A

### ThreadedTask
Creates threaded tasks for the tkinter GUI

| Dependencies | Members | Functions |
| --- | --- | --- |
| tkinter| queue - Queue | \_\_init\_\_(Queue,Function)|
| threading | function - Function | run() |

**ThreadedTask.\_\_init\_\_(self,queue,function)**

    -- Description --
    Creates a TeadedTask object which will run a desired function.

    -- Parameters --
    queue - a Queue object
    function - the function that will be run by this thread.

    -- Returns --
    N/A

**ThreadedTask.run(self)**

    -- Description --
    Runs the function that self.function points to.

    -- Parameters --
    N/A

    -- Returns --
    N/A

## Functions
* [filters](#filters)
* [io_functions](#io_functions)
* [inform](#inform)

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

### inform

| Dependencies | Functions|
| --- | --- |
| Team | valid_config(ConfigData) |
| Student | parse_email(str,str,str) |
| ConfigData | send_email(Team,str,str)  |
| MIMEText | parse_team_file(file) |
| smtplib | send_email_cmdline(Arguments) |
| getpass | |
| argparse | |
| os | |

**valid_config(cnfg)**

    -- Description --
    Checks that the config settings are valid. This is only checking that all
    required settings are supplied and returns true or false.

    -- Parameters --
    cnfg - the ConfigData settings being used

    -- Return --
    a boolean

**parse_email(filename,receiver,sender)**

    -- Description -- 
    Loads the specified email template and parses it into a subject and body for the email.

    -- Parameters --
    filename - the emailtemplate to be used
    receiver - the names of the recipients of the email
    sender - the name of the sender of the email

    -- Return --
    a tuple in the form (subject, body)

**send_email(team, usr, passwrd)**

    -- Description -- 
    Sends the email to the people within the Team team. Returns True of False
    depending on the results of sending the email. *Note* a True return doesn't
    guarantee delivery, it only means the SMTP didnt return an error and has
    made an attempt to deliver the emails.

    -- Parameters --
    team - a Team that is to be emailed
    usr - the smtp login, defaults to an empty string
    passwrd - the smptp password, defaults to an empty string

    -- Return --
    a boolean

**parse_team_file(file)**

    -- Description -- 
    Parses an output file from the main TeamBuilder2.0 application so that
    teams may be informed via commandline.

    -- Parameters --
    file - the output file that contains the final teams.

    -- Return --
    a Team[]

**send_email_cmdline(args)**

    -- Description -- 
    Sends the emails to the teams via a commandline call. Prompts for username
    and password, via stdin, to the SMTP server specified in config settings.

    -- Parameters --
    args - Argument object that contains the arguments passed at command line.

    -- Return --
    N/A

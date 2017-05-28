# Team Builder Project 2.0

 Authors: Garett Roberts, Alister Maguire, Jared Paeschke, Howard Lin 

 Contact:
  * Alister: aom@uoregon.edu
  * Garett:  groberts@uoregon.edu
  * Howard:  howardl@uoregon.edu
  * Jared:   jpaeschk@uoregon.edu


## Purpose
 
 The primary purpose of the Team Builder is to assign students to 
 teams of a given size. These teams are created with various 'filters'
 in mind to optimize the success of the teams. For instance, available
 times for team meetings is considered a filter that helps match students
 with one another. 

 Currently, there are three filters used in team creation, and they are as
 follows:

    * availability for metting times
    * prefered group members
    * shared programming languages

 By default, all filters are given the same weight. However, you can easily 
 change the weight alloted to filters within the config folder. For instructions
 on altering filter weight, see the configuration guide within the config directory. 


## Installation and Dependencies

 There are two dependencies for Team Builder: python 3.x, such that 
 x >= 4, and Tkinter.  

 In a similar vein, there is no extensive installation needed for Team Builder. 
 You merely need to download the project and run the python scripts, which can
 be accomplished by the following steps:

 step 1: 
     Go to the main repo on github https://github.com/garetroy/TeamBuilder2.0
    
 step 2: 
     Once at the main repo, you will see a green button titled "Clone or download".
     Click this button, and click 'DOWNLOAD ZIP' in the drop down menu that appears. 
     This will download the repo as a compressed file. 

 step 3:
     Unzip the file. 

 You're done!
     


## Directory Structure
 
 The directory stucture is as follows:


                               TeamBuilder
                                    |
            ----------------------------------------------------
            |           |           |           |              |
         config        data         doc         src            test
                                                               |
                                                        -------------------
                                                        |         |       |
                                                    baseline   results   tests


 This structure is rather self explanatory:
 Data is contained within the data directory, documentation is 
 contained within doc, source code is contained within src,
 the test suite is contained within test, and configuration 
 options are within config. 
 
 Within each directory, excluding doc, there is a general README conveying what
 is contained within that directory. The doc directory is excluded from this 
 convention as it holds extensive documentation. 

 For further documentation, including user and developer guidelines, visit the
 doc directory. 


## Basic Usage

### Start-up

* **Linux/Unix**:
  For users who are using Linux/Unix OS, you can invoke the program by invoking
  the run bash script located in the main repo directory. If using bash, this 
  script can be invoked through a terminal as follows:

  ```
  bash run
  ```

* **Non-bash systems**:
  For non-bash systems, the program can be invoked directly with python3. 
  To do this from the main directory repo, type the following command 
  into a terminal:

  ```
  python3 src/gui.py
  ``` 

### Input

  After invoking the program, you will see a basic user interface with the 
  following entry boxes:

  * Path to csv: the path to your csv input file. This is the file 
    containing all of your student's survey data. 

  * Path to roster: the path to a roster file. See the section labeled
    [**Other**](#Other) for details on how to format the roster file. 

  * Path to output: the path to the output directory. 

  * Team size: the desried team size. If the number of students is not 
    divisible by this target size, then the excess students will be 
    distributed among the allocated teams, resulting in some teams 
    being one larger than the desired team size. 
               
### Running the Program

  After all entry boxes have been filled, you can invoke the algorithm by 
  clicking "Submit". You should see a progress screen notifying you
  that the algorithm is running. Once finished, you will see a list of the 
  allocated teams along with assigned scores. The scores range from 0.0 to 
  1.0, representing a scale of 0% to 100%, worst to best. 

  * **Re-running**: you can re-run the algorithm by clicking 'Rerun'. 

  * **Shuffling team members**: you can shuffle team members from any number
    of teams by first selecting the target teams and then clicking 
    'Shuffle Selected'. Selecting the target teams is simply a matter
    of clicking on them. You will see the selected teams become highlighted, 
    denoting their selection. You can click on a team once more to 
    un-highlight/de-select them. 

  * **Swap individual members**: you can also swap specific members between 
    two teams at a time. To do so, select two teams, and click 
    'Swap Members'. Once done, a new window will open showing the
    teammates from each team. You can select a teammate from either
    team and swap it to the opposite by clicking 'Swap Team'. 

  * **Inspection**: you can inspect teams more closely by double clicking on
    them. Once done, a new window will open showing team details. 

  * **Saving output**: once you are satisified with the team selections, you
    can save them to your output destination by clicking "Save". The
    teams will be output using the writer format that is currently 
    enabled. By default, a basic txt writer is used to create a text
    file with the name 'out.txt'. The format of this writer's output 
    is as follows:

    Team number
    Team score
    Team members:
    1.
    2.
    .
    .
    .
    n.

  * **Emailing results**: you can send out a mass email informing students of
    their selected teams by first selecting the teams you wish to email
    and then clicking 'Email'. A window will pop up asking for you email
    and password. For details on how to configure the body of the email,
    see the configuration documenation in the config directory.    
  

## Other <a name="Other"></a> 

  * **Roster specifications**: the roster is a new line deliniated list including
    but not limited to all of the students participating within the team
    building selection.

    The roster is used for two reasons; first, it allows the app to verify 
    that a survey submission is from a valid student. Second, and most 
    importantly, it allows the app to search for and correct spelling 
    errors that may occur. For instance, if a student wishes to work
    with a particular classmate but accidentally misspells their classmate's
    name, the roster will increase the chances of the app being able to
    find and correct this misspelling without bothering the user of the app.
    If a match cannot be found for a particular name, then an error will
    be raised so that the user of the app can inspect the problem themselves. 

    The roster should be saved as a .txt file and should be formatted as follows:

    last_name, first_name
    last_name, first_name
    .
    .
    .


  * **Configuration**: there are multiple configuration and extension options for 
    this app, all of which can be accessed within the config directory. 
    For detailed information on configuration and extension, you should 
    read the configuration documentation that is located in the config 
    directory. What follows is only a brief summary of the configuration 
    and extensions available to you:

    Configuration:
    * Applying weights to filters   
    * Changing default reader and writer
    * Configuring email template

    Extension:
    * Adding readers and writers
    * Adding filters 
        

  * **Documentation and User Guide**: for further documentation, including devloper
    documentation and a user guide, visit the doc directory. 

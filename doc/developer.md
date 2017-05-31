
# Development Documentation

 This section is dedicated to answering questions that pertain to
 extending the Team Builder application. 

 First, before extending the code base for Team Builder, make sure 
 that you have familiarized yourself with the testing suite and 
 thoroughly read through the README located in that directory. 

 As it is impossible for us to predict all of the desired extensions
 that a future developer may seek to add to this project, we can only
 do our best in addressing the issues/questions that are most likely 
 to arrise. If there are any remaining unanswered questions, feel 
 free to contact us directly for further assistance. 

 What follows is an overview of some of the most likely areas to be
 considered for extension and the types of concerns and dependencies
 that must be taken into consideration. 

 Before reading on, it should be noted that there are two areas of 
 development that have been specifically desinged for easy extension. 
 These areas are as follows:

 **IO extensions**: adding readers and writers.
 **Filters**: adding new filters for comparing students. 

 For guidelines in extending either of these two features, visit the 
 config directory, and read the documentatino located there. For 
 development of all other features, read on. 


## GUI
 -Requires guiinterface
 
 The gui was created with the developer in mind, so it is simple to modify and
 tweak the program to the individuals liking. Most of the logic is contained
 within the gui interface. 

 The centerWindow function does as you expect, it centers the window,
 the only difference being that if notself is given, it assumes
 that the window given is going to be a smaller screen (such as a login or 
 a loading screen), and changes the size then centers the given window.

 startWindow set's up the basic setup for all windows, centering the window
 and setting the style.

    **Start UI**
    All UI components dealing with layout will be commented in a readable format
    where it will have a # letting you know where the created frame is starting
    and ending. Most frames will be self explanitory in this way and will not
    be explained unless some odd things are contained within the function.

    emailTeams stores everything needed into the guiInterface (expecially if the
    user desires to have the email/password saved).
    
    In loadingScreen it is important to know that it disables all buttons
    for the current frame.

 In submitFiles we are checking to see if the paths exists and are also
 checking if the team size values are valid.

 checkThread was important to implement, so we would know when to get rid
 of the current loading screen. It just calls itself every second to check
 if it is dead, and if it is, it calls the given function.

 All filebrowsers work the same, they just look for different types of 
 file extensions, chaning the corresponding label to what was given 

    **ThreadedTask**
    This is just our thread pool for threaded tasks. This is important
    for the smooth running of the gui.
 
## GUI Interface
 -requires day
 -requires team
 -requires student
 -requires inform
 -requires algorithm
 -requires iomanager
 -requires configdata
 
 A lot of these functions are pretty self explanitory trhoguh their names,
 but will still be described if they are doing something funky. 

 reShuffleSelectedTeams takes in a corresponding list of indexes to teams.
 It utilizes the swapMembers algorithm and then appends the newly shuffled
 teams to the end of the list

 sendEmail has a lot of moving parts. The only thing required for paramaters
 is teams. This is because if the user already specified to temporarily
 store their email/password, then we wouldn't have to keep passing those 
 parameters. The rest of the block of code simply just sends emails to the
 corresponding teams and if specifided, stores the email and password
 for ease of use


## Algorithm

 Dependencies:
 Student
 Team
 Filters
 SwapList

 As you might expect, the algorithm is the main engine for matching up students
 and forming groups. It takes in a list of Student objects and does its best 
 to create the best overall teams it can. 

 The algorithm works as follows: 
 * Create 'k' sets of randomly chosen teams.
 * For 'd' number of iterations, do the following:
    * Remove one set of teams from the initial set.
    * Create 'n' new sets of teams by randomly swapping group members bewteen 
      teams. 
    * Choose the "best" set of teams, and add it back to the main set that was
      first initialized. 
    * Do that 'k' times.
 * Choose the "best" set of teams out of the final set of teams. This is now
   the result of the algorithm.

 It's a mouthful, but that is our algorithm in a nutshell. There are a couple more 
 details that need explanation, though. 
 The "best" set of teams is defined as the set of teams with the highest overall 
 score and the lowest deviation (difference between highest scoring team and lowest
 scoring team). This is simply calculated as (sum of all socres) - (high score - 
 low score).

 It should also be noted that the scores are continuously normalized so that they
 remain as a floating point value between 0.0 and 1.0 (inclusive). 


## IOManager

 The IO manager is the module that calls the functions implemented within the 
 configuration directory. This module also handles parsing the roster file, and
 it is here that spelling errors are checked. If you'd like to change the way in
 which spelling errors are handled (increase or decrease sensitivity), then this
 is the place to do it. 


## SwapList

 The SwapList module is a very simple extension of a basic python list which 
 adds a new way of popping from an arbitrary index without the increased time
 complexity generally associated with this act. The added method is called
 'popSwap', and it swaps the last element with the desired pop element, and
 then pops off the end. In this manner, time complexity remains constant. 


## ConfigData

The ConfigData module is use for communicating configuration information to the 
rest of the modules within the src directory. The module simply reads in and parses
the data from config.json, and this data is then stored in structures that can be
accessed from the outside world. 


## Other

 The remaining modules that haven't yet been covered are generally simple containers
 for storing data. For example, Student is merely an object to hold data relating 
 to students. As these modules are easily understood by peeking at the source code, 
 their coverage is being omitted in this section. 


 

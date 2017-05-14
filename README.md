
 ***Team Builder Project***

 Authors: Garett Roberts, Alister Maguire, Jared Paeschke, Howard Lin 

 Contact:
    Alister: aom@uoregon.edu
    Garett:  groberts@uoregon.edu
    Howard:  howardl@uoregon.edu
    Jared:   jpaeschk@uoregon.edu


 **Purpose**
 
 The primary purpose of the Team Builder is to assign students to 
 teams of a given size. These teams are created with various 'filters'
 in mind to optimize the success of the teams. For instance, available
 times for team meetings is considered a filter that helps match students
 with one another. 

 Currently, there are three filters used in team creation, and they are as
 follows:

     *availability for metting times*
     *prefered group members*
     *shared programming languages*

 As of now, these filters are all given equal weight. However, it is currently
 quite easy to change the weight assignments, and we plan to allow user input
 to decide these weights in the near future. 


 **Installation and Dependencies**

 The only dependency for Team Builder is python 3.x, such that x >= 4.

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
     


 **Directory Structure**
 
 The directory stucture is as follows:


                                TeamBuilder
                                     |
                    ----------------------------------------
                    |           |           |              |
                  data         doc         src            test
                                                           |
                                                    -------------------
                                                    |         |       |
                                                baseline   results   tests


 This structure is rather self explanatory:
 Data is contained within the data directory, documentation is 
 contained within doc, source code is contained within src, and 
 the test suite is contained within test. 
 
 Within each directory, excluding doc, there is a general README conveying what
 is contained within that directory. The doc directory is excluded from this 
 convention as it holds extensive documentation. 

 For further documentation, including user and developer guidelines, visit the
 doc directory. 


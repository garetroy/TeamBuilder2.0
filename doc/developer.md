
 ***Development Documentation***

 This section is dedicated to answering questions that pertain to
 extending the Team Builder application. 

 First, before extending the code base for Team Builder, make sure 
 that you have familiarized yourself with the testing suite and 
 thoroughly read through the readme located in that directory. 

 As it is impossible for us to predict all of the desired extensions
 that a future developer may seek to add to this project, we can only
 do our best in addressing the issues/questions that are most likely 
 to arrise. If there are any remaining unanswered questions, feel 
 free to contact us directly for further assistance. 

 What follows is an overview of some of the most likely areas to be
 considered for extension and the types of concerns and dependencies
 that must be taken into consideration. 

 **IO Management**

 It is very likely that a developer may want to extend this project
 to be capable of handling different types of input and output. Fortunately, 
 this is a rather easy objective as IO is entirely contained with a single module, 
 iomanager.py (I will, from here on, refer to this module as the IO manager). 

 The IO manager is designed to make extension as painless as possible. If 
 you wish to add a new method for reading or writing, there are really only 
 three steps to consider (four, if you include testing). The first step is to 
 creat a new method within the IO manager that will handle the new reading 
 or writing. 


   __IMPORTANT__: all writers must take the following form--

   myWriter(self, path, teams)

   where 'myWriter' is replaced with the name of your new write method, path
   is the system path to the output file (file name included), and teams is a 
   list of Team objects. 

   In the same manner, all readers must take the following form--

   myReader(self, path)

   where 'myReader' is replaced with the name of your new read method, and 
   path is the system path to the file to be read in. 

 
 The second step in creating a new reader or writer is to add this new method
 to the appropriate reader/writer dictionary (both located in the initializer).
 There are two dictionaries for this purpose, one for writers and one for readers. 
 Each dictionary associates a reader/writer name, respectively, with the a pointer
 to the associated method. For instance, if I created a new reader called dataBaseReader,
 I would add this reader to the dictionary as follows:

 self.\_\_readers = {'dataBase' : self.dataBaseReader}

 Note that, in this example, there are no other readers in the dictionary. This will
 not be the case. You will instead be adding your reader in to a collection of readers
 within the dictionary. Also, 'dataBase' is an arbitrary name that I made up. There
 are no established conventions on the naming of these readers or there dictionary keys, 
 as long as they are understandable to a new user. 

 The final step is to add the name/key of your reader/writer (the name you are using as a 
 key in the dictionary) to the list of accepted input or output. These lists are also 
 located within the initializer. 

 For instance, following the above example, I would add the key in the following manner:

 self.\_\_accepted\_in = ['dataBase', '']

 Again, this example is unrealistic, as there are no other elements in the list, but this
 gives you an idea of the simple process for extending IO management. 

 And that's it! You have now added a new read/write method to the Team Builder project!

 
 
 

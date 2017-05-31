This folder contains the configuration files. 



 A filter allows for a developer to add more things to compare or how to compare two 
 students on certain criteria. To develop (or modify) a filter is made pretty easy.

   __IMPORTANT__: all filters must have the following form--
   myFilter(student1, student2)

   'Filtername'

   student1 and student2 are the students that we are taking in, they variables can be 
   named differently. Filtername is the ID that you want to give the filter, which will
   be used to recieve the cresidentails from the individual students.

   Filtername will be added to the student at IO for the filters that you want to import

At the end the filter must return a score for the two students.





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


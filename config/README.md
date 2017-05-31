
# Configuration


## Basic Configuration Options

**Note**: You will see the word "Filter" arrise throughout this documentation, 
    and thus it is important to understand how we are defining this word. A 
    Filter, in our context, is a module which compares two students and procues
    a score representing the compatibility of two students within a group. 


### Filter Weights

 In all likelihood, users will want to change the weights associated with various
 filters. Changing filter weights essentially allows users to place greater/lesser
 importance on select filters. 

 **Setting Weight**:
 Within the config.json file, you will see a section labeled "filters" which 
 should resemble the following:

 '''
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "1"],
        "Languages"  : ["languageFilter", 3, "1"],
        "Teammates"  : ["teammateFilter", 2, "1"] 
    },
 ''' 

 In short, "filters" is a list of dictionaries where the keys are filter identifiers
 and the values are lists containing the following information:

 '''
 [ filter/_function/_name, maximum/_elements, weight ]
 '''

 For setting weights, all you need to be concerned about is the last element, which 
 is the weight associated with that filter. **By changing this value, you directly change
 the weight attributed to that filter**. However, there is one important restriction
 to assigning weights; **the sum of the weights MUST equal the number of filters in 
 the config.json file**. This allows for consistent normalization to occur within the
 algorithm.  
 For example, if you wanted to have twice as much importance placed on student's 
 schedules while maintaining an even balance between Languages and Teammates, then 
 you would alter the filter weights like so:
 
 '''
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "2"],
        "Languages"  : ["languageFilter", 3, ".5"],
        "Teammates"  : ["teammateFilter", 2, ".5"] 
    },
 ''' 

 As you can see, the weights are floating point values. If accidentally enter weights
 that do not sum to the number of filters, an error will be thrown when running the
 algorithm. 


### Default IO

 By default, the algorithm will use a txtWriter for writing and a csvReader for reading. 
 If you would like to change the default reader/writer, you merely need to replace the 
 corresponding reader or writer in the default setting. 
 For instance, the current defaults section resembles the following:

 '''
    "defaults" :
    {
        "rdr" : "csv",
        "wrtr": "txt"
    },
 '''

 Let's say that you create reader which reads in text data and that the name of this
 reader is TxtReader. If you wanted the app to use this reader by default, you would
 change the defaults section like so:

 '''
    "defaults" :
    {
        "rdr" : "TxtReader",
        "wrtr": "txt"
    },
 '''


## Developig New Filters

 Adding new filters is generally pretty straight forward and can be thought of as 
 consisting of a few steps which are outlined below.

 * Step 1:

    Write a filter module within the filters.py file.  

   _**IMPORTANT**_: all filters must have the following form--

   ```
   def myFilter(student1, student2)
   .
   .
   .
   ```

   student1 and student2 are the students that are being compared for compatibility. 
   _**IMPORTANT**_: All filters must return a floating point value between 0.0 and
   1.0 inclusive, 0.0 representing no match at all and 1.0 representing the best
   match possible. 

 * Step 2:
    
    Filters generally rely on incoming data, which means that you must incorporate
    reading this data into whatever reader you are using. For instance, if you are
    using the csvReader and would like to add a new filter which matches students
    on their gpa, then you will likely have a section in your survey which asks for
    students gpa (of course, there are other ways to get this information, but I 
    will stick with this for simplicity). 


















***INCOMPLETE***




   **IMPORTANT**: all writers must take the following form--

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


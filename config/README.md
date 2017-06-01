
# Configuration


## Basic Configuration Options

**Note**: You will see the word "Filter" arrise throughout this documentation, 
    and thus it is important to understand how we are defining this word. A 
    Filter, in our context, is a module which compares two students and produces
    a score representing the compatibility of two students within a group. 


### Filter Weights

 In all likelihood, users will want to change the weights associated with various
 filters. Changing filter weights essentially allows users to place greater/lesser
 importance on select filters. 

 **Setting Weight**:
 Within the config.json file, you will see a section labeled "filters" which 
 should resemble the following:

 ```
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "1"],
        "Languages"  : ["languageFilter", 3, "1"],
        "Teammates"  : ["teammateFilter", 2, "1"] 
    },
 ``` 

 In short, "filters" is a list of dictionaries where the keys are filter identifiers
 and the values are lists containing the following information:

 ```
 [ filter_function_name, maximum_elements, weight ]
 ```

 For setting weights, all you need to be concerned about is the last element, which 
 is the weight associated with that filter. **By changing this value, you directly change
 the weight attributed to that filter**. However, there is one important restriction
 to assigning weights; **the sum of the weights MUST equal the number of filters in 
 the config.json file**. This allows for consistent normalization to occur within the
 algorithm.  
 For example, if you wanted to have twice as much importance placed on student's 
 schedules while maintaining an even balance between Languages and Teammates, then 
 you would alter the filter weights like so:
 
 ```
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "2"],
        "Languages"  : ["languageFilter", 3, ".5"],
        "Teammates"  : ["teammateFilter", 2, ".5"] 
    },
 ```

 As you can see, the weights are floating point values. If you accidentally enter weights
 that do not sum to the number of filters, an error will be thrown when running the
 algorithm. 

<a name="defaults"></a>
### Default IO 

 By default, the algorithm will use a txtWriter for writing and a csvReader for reading. 
 If you would like to change the default reader/writer, you merely need to replace the 
 corresponding reader or writer in the default setting. 
 For instance, the current defaults section resembles the following:

 ```
    "defaults" :
    {
        "rdr" : "csv",
        "wrtr": "txt"
    },
 ```

 Let's say that you create reader which reads in text data and that the name of this
 reader is TxtReader. If you wanted the app to use this reader by default, you would
 change the defaults section like so:

 ```
    "defaults" :
    {
        "rdr" : "TxtReader",
        "wrtr": "txt"
    },
 ```


## Developig New Filters

 Adding new filters is generally pretty straight forward and can be thought of as 
 consisting of a few steps, which are outlined below.


 * Step 1:
    
    Filters generally rely on incoming data, which means that you must incorporate
    reading this data into whatever reader you are using. For instance, if you are
    using the csvReader and would like to add a new filter which matches students
    on their gpa, then you will likely have a section in your survey which asks for
    students gpa (of course, there are other ways to get this information, but I 
    will stick with this for simplicity). 

    Whatever type of reader you are using, it will need to follow the guidlines
    outlined in [**IO Development**](#Readers). This means that you will 
    need to read in the data from your source and save this data into a filters
    dictionary. See the developing readers section for more information and examples
    pertaining to adding data to the filters dictionary.  

 * Step 2:

    Write a filter module within the filters.py file. As stated earlier, filters 
    are a means of comparing two students and determining a score based on some
    kind of criteria. The Student objects themselves have a dictionary containing
    all of the filter data (their schedule, lanugage preferences, etc.) that comes
    from the student survey. You can then easily access these preferences directly 
    from each student and use them for comparison. 
    How exactly two students are compared is left up to you, but there are a couple
    rules which must be adhered to:

   **IMPORTANT**: all filters must have the following form:

   ```
   def myFilter(student1, student2)
       .
       .
       .
       return score
   ```

   where student1 and student2 are the students that are being compared for 
   compatibility. 

   **IMPORTANT**: All filters must return a floating point value between 0.0 and
   1.0 inclusive, 0.0 representing no match at all and 1.0 representing the best
   match possible. 


 * Step 3:
    
    Lastly, you will need to update the config.json file to include your new filters.
    This is simply a means of adding your new filter to the "filters" section in 
    the json. For instance, let's say you create a filter called "GPAFilter". Since
    every student has exactly one GPA, the number of elements associated with the 
    GPAFilter is at most one (for a language filter, you might allow students to include 
    3 languages that they prefer, which would mean the number of elements is at 
    most 3).  

    If the "filters" section in the json looks like the following before adding 
    your GPAFilter,

    ```
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "1"],
        "Languages"  : ["languageFilter", 3, "1"],
        "Teammates"  : ["teammateFilter", 2, "1"] 
    },
    ```

    then your addition would look something like the following:

    ```
    "filters" :
    {
        "Schedule"   : ["scheduleFilter", 13, "1"],
        "Languages"  : ["languageFilter", 3, "1"],
        "Teammates"  : ["teammateFilter", 2, "1"],
        "GPA"        : ["GPAFilter", 1, "1"]
    },
    ```

    The format of the "filters" elements is as follows:

    ```
    key : [ name_of_filter_function, max_num_of_elements, weight ] 
    ```

    where 'key' is a keyword used as a key in this dictionary (just use something
    that is representative of the filter), 'name\_of\_filter_function' is a string
    representation of the filter function's name, 'max\_num\_of_elements' is the 
    maximum number of elements associated with this filter while reading in your
    survey data (as an int), and 'weight' is a string representation of the weight
    attached to this filter. 
    

<a name="Readers"></a>
## IO Development
 
 This section is for assisting in the development of readers and writers, both
 of which should be relatively simple. 

 The first step for adding a new reader or writer to the TeamBuilder app is to
 write a reader/writer module within the io\_functions.py file. The guidelines
 for development are as follows:

**Readers**:
 
   All readers must take the following form:

   ```
   def myReader(iomanager, path):
       .
       .
       .
       return students
   ```

   where 'myReader' is replaced with the name of your new read method, 
   path is the system path to the file to be read in, iomanager is a reference
   to an IOManager object (explained below), and students is a list of student 
   objects. 
 
   The primary job of readers are to read in student survey data and create 
   student objects consisiting of this data. These student objects are then
   placed into a list which is returned after all data has been read. 

   Student objects require a name and email for construction, as shown below:

   ```
   student = Student("alfred", "alfred@mailcarrier.com")
   ```

   As such, your survey data should associate names with student responses. 

   Another key aspect to Student objects is the filters dictionary, which is where
   most of the reader's effort is focused. The filter dictionary has the following
   form:

   ```
   filters['key'] = ( list_of_response_elements, max_length_of_list, filter_weight )
   ```

   That is, the filter dictionary is a tuple where the first element is a list, the 
   second is an int, and the third is a string representation of a floating point 
   value. 

   **Important**: the filters dictionary is MUST be populated through accessing 
   a special data structure called "c\_data", which holds all of the data contained 
   within the config.json file. c\_data can be accessed directly through the iomanager,
   which is a required argument for the reader. For instance, the following would
   be a direct access to c\_data:

   ```
   iomanager.c_data
   ```

   Within the c\_data object is an object called "filters\_dictionary", which allows
   directy access to all of the filter information. This is how you will populate the
   "max\_length\_of\_list" and "filter\_weight" aspects of the Student object's filter
   dictionary. 

   For example, building on the GPAFilter example, we would first pull in the GPA data
   from our data source and store this in a list. In this case, each student would have
   a list of length 1 containing their GPA. Let's call this list gpa\_lst, and the 
   following is how we would add this filter to the student's filter dictionary:

   ```
   filters["GPA"] = (gpa_list, iomanager.c_data.filter_dictionary["GPA"][1],
                     iomanager.c_data.filter_dictionary["GPA"][2] )
   ``` 

   As you can see, the first element is the only element that is created in the reader.
   The remaining two are taken from c\_data. It's also important to note that the key
   in the student's filters dictionary matches the key in the filters dictionary within
   the config.json file. The retrieval of data from c\_data is a bit verbose, but it's 
   mere grabbing the second element of the "GPA" value, which is the maximum length
   of the data list, and the last element, which is the weight for that filter.   

   After creating your reader module, you will want to add it to the config.json file. 
   For instance, if you were to create a reader called TextReader, then you could add 
   it like so:

   ```
    "readers" :
    {
        "csv" : "csvReader"
        "TxtRdr" : "TextReader"
    },
   ```

   If you'd like to enabel your new reader by default, then you will also want to add 
   it to the [**defaults**](#defaults) section of the config.json file. 

**Writers**:

   All writers must take the following form:

   ```
   def myWriter(iomanager, path, teams):
       .
       .
       .
   ```

   where myWriter is to be replaced by the name of your writer module, iomanager is an 
   IOManager object (may not be used), path is a path to the output destination, and 
   teams is a list of Team objects. 

   Aside from the above restrictions, how the writers function is complete up to you!

   The last step for creating a writer is to add it to the config.json file. If you've
   created a MarionBerryWriter, you would add it like so:

   ```
    "writers" :
    {
        "txt" : "txtWriter",
        "score" : "scoreWriter"
        "MBWriter" : "MarionBerryWriter"
    },
   ```

   If you'd like to enabel your new writer by default, then you will also want to add 
   it to the [**defaults**](#defaults) section of the config.json file. 
   


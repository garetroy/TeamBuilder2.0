
  This directory contains the test suite used in testing the Team Builder application. 

**When extending the existing code for Team Builder, it is important to run the test
  suite to make sure that your extensions have not had unexpected results.**

  Currently, the test suite is set up to be used in a bash environment, and it has been 
  successfully tested on both Linux (Debian) and Mac. If you are using a different OS, 
  especially Windows, then you will likely need to make alterations to fit the needs
  of your OS. In particular, the runtests script will need to be altered, and the method
  for retrieving directories within the python tests (located in test/tests/) will 
  also need to be altered. 

 **Running the test suite with bash**

   To run the test suite using bash, type the following and press enter:

   bash ./runtests.sh
   
   runtests is currently set up to invoke python by using 'python3 ...'. 
   If your OS is set up to invoke python 3 by using 'python ...' or some
   other naming convention, then you can easily fix this by opening the 
   runtests script and changing "PY VAR" to equal whatever name your OS
   uses to invoke python3. 
   
   If all goes well, then you will see output of the following form:
   ```
   testFoo passed
   testBar passed
   .
   .
   .
   ```
   
   If, however, you see a failure, the results of the failed tests
   will be located in the test/restuls directory. You can then diff
   the output in the test/results directory with the same named file
   in the test/baseline directory to see what went wrong. 
   
   
**Adding and editing tests in the suite**

  The tests run in the test suite are located in /test/tests/

  Editing existing tests is discouraged, unless absolutely necessary. 
  This is generally only necessary when altering existing code in 
  such a way that the results from the test outputs are expected to 
  be different than there current state. If this is the case, be sure
  to make sure and check that the new output is correct. 

  To add a new test to the suite, you can write a test script, add 
  this script to the tests directory, and then add the invocation 
  to the runtests script. You will also need to create an output 
  with the correct results and add this to the baseline directory,  
  located at test/baseline/. This will allow for the runtests script
  to check the current results against the baseline results. 
  It is highly encouraged that all developers add new tests to the 
  suite after making significant alterations or extensions to the 
  code base. 

  By convention, all data used in the test suite is located in the 
  /data directory.  
  




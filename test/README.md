This directory contains the test suite used in testing the Team Builder application. 

*When extending the existing code for Team Builder, it is important to run the test
 suite to make sure that your extensions have not had unexpected results.*

Currently, the test suite is set up to be used in a bash environment. If you are using windows,
you can use Cygwin to run the test suite. Otherwise, you may want to create your own runtests
script that is compatible with your personal OS.

 **Running the test suite with bash**

   To run the test suite using bash, type the following and press enter:

   bash ./runtests.sh
   
   runtests is currently set up to invoke python by using 'python3 ...'. 
   If your OS is set up to invoke python 3 by using 'python ...' instead, 
   then you will see an error raised regarding python3 not being a recognized
   command. If this is the case, you can easily fix this by changing the 
   instances of 







#!/bin/bash


$PY_VAR=python


#iotest1
$PY_VAR tests/iotest1.py ../data/small_data.csv ../data/small_roster.txt > results/iotest1
DIFF=$(diff results/iotest1 baseline/iotest1)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "iotest1\n"
    #printf "$DIFF\n\n"
else
    printf "iotest1 passed!\n"
fi
 
#iotest2
$PY_VAR tests/iotest2.py ../data/small_data.csv ../data/small_roster.txt results/iotest2
DIFF=$(diff results/iotest2 baseline/iotest2)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "iotest2\n"
    #printf "$DIFF\n\n"
else
    printf "iotest2 passed!\n"
fi

#schedule test 1
$PY_VAR tests/scheduleTest.py ../data/medium_data.csv ../data/large_roster.txt > results/s1_test
DIFF=$(diff results/s1_test baseline/s1_test)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "s1_test\n"
    #printf "$DIFF\n\n"
else
    printf "s1_test passed!\n"
fi

#teammate test 1
$PY_VAR tests/teammateTest.py ../data/medium_data.csv ../data/large_roster.txt > results/mate_test1
DIFF=$(diff results/mate_test1 baseline/mate_test1)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "mate_test1\n"
    #printf "$DIFF\n\n"
else
    printf "mate_test1 passed!\n"
fi


#language test 1
$PY_VAR tests/langTest.py ../data/medium_data.csv ../data/large_roster.txt > results/lang_test1
DIFF=$(diff results/lang_test1 baseline/lang_test1)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "lang_test1\n"
    #printf "$DIFF\n\n"
else
    printf "lang_test1 passed!\n"
fi

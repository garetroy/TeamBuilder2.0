#!/bin/bash

#iotest1
python3 tests/iotest1.py ../data/small_data.csv ../data/small_roster.txt > results/iotest1
DIFF=$(diff results/iotest1 baseline/iotest1)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "iotest1\n"
    printf "$DIFF\n\n"
else
    printf "iotest1 passed!\n"
fi
 
#iotest2
python3 tests/iotest2.py ../data/small_data.csv ../data/small_roster.txt results/iotest2
DIFF=$(diff results/iotest2 baseline/iotest2)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "iotest2\n"
    printf "$DIFF\n\n"
else
    printf "iotest2 passed!\n"
fi

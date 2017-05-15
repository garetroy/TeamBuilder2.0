#!/bin/bash

#note: changing PY_VAR will change the name used to 
#      invoke python 3
PY_VAR=python3


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
    rm results/iotest1
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
    rm results/iotest2
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
    rm results/s1_test
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
    rm results/mate_test1
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
    rm results/lang_test1
fi


#perfect score test 
mkdir ../src/safe
mv ../src/config.json ../src/safe
cp ../data/config_tester1.json ../src/config.json

$PY_VAR tests/scoreTest.py ../data/tiny_data.csv ../data/tiny_roster.txt ./results/perfect_team

mv ../src/safe/config.json ../src/
rmdir ../src/safe

head -n2 results/perfect_team > results/tmp
mv results/tmp results/perfect_team

DIFF=$(diff results/perfect_team baseline/perfect_team)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "perfect_team\n"
else
    printf "perfect_team passed!\n"
    rm results/perfect_team
fi


#perfect score test 2
mkdir ../src/safe
mv ../src/config.json ../src/safe
cp ../data/config_tester2.json ../src/config.json

$PY_VAR tests/scoreTest.py ../data/tiny_data.csv ../data/tiny_roster.txt ./results/perfect_team2

mv ../src/safe/config.json ../src/
rmdir ../src/safe

head -n2 results/perfect_team2 > results/tmp
mv results/tmp results/perfect_team2

DIFF=$(diff results/perfect_team2 baseline/perfect_team2)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "perfect_team2\n"
else
    printf "perfect_team2 passed!\n"
    rm results/perfect_team2
fi



#perfect score test 3
mkdir ../src/safe
mv ../src/config.json ../src/safe
cp ../data/config_tester2.json ../src/config.json

$PY_VAR tests/scoreTest.py ../data/one.csv ../data/two_perfect_teams_roster.txt ./results/perfect_team3

mv ../src/safe/config.json ../src/
rmdir ../src/safe

head -n2 results/perfect_team3 > results/tmp
mv results/tmp results/perfect_team3

DIFF=$(diff results/perfect_team3 baseline/perfect_team3)

if [ "$DIFF" != "" ]
then
    printf "\nTEST FAILED: "
    printf "perfect_team3\n"
else
    printf "perfect_team3 passed!\n"
    rm results/perfect_team3
fi

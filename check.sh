#!/bin/bash
result=0
for file in `ls trainall/`; do
    retVal=`python3 inf132275_inf132332.py trainall/$file`
    correctGender=`echo $file | sed 's/.*_\(.*\).wav/\1/'`
    if [ $correctGender = $retVal ]; then
        echo $file 'Correct'
        ((result++))
    else 
        echo $file 'INCORRECT'
    fi
done
echo $((result*100/93))
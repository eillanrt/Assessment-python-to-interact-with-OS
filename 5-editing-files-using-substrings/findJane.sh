#!/bin/bash

grep " jane " list.txt | cut -d ' ' -f 3 | while read -r line ; do
    # echo "Processing $line"
    # your code goes here
    file_name="$line"

    if test -e "$file_name"; then
     echo $file_name exists...
     echo $file_name >> oldFiles.txt
    else 
     echo $file_name does not exist...
    fi
done
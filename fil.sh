#!/usr/bin/env bash

files_list=$(ls)
files=0
for file in $files_list:
do
	if [ "$file" != "fil.sh" ]
	then
		files=$((files + 1))
	fi
done
echo "Total number of files: $files files"

#!/usr/bin/env bash

files_list=$(ls)
for file in $files_list:
do
	git add "$file"
	git commit -m "$file"
	git push
done

echo "EVERYTHING pushed"
git status

#!/bin/bash

for var in `ls`
do
	if
		[ -f $var ]
	then
		echo $var is a regular file
	fi
done

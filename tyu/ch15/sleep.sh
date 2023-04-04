#!/bin/bash

while
	[ test1 -nt test2 ]
do
	echo sleeping ...
	sleep 10
	echo ...
	sleep 10
	echo ...
done

echo Done!

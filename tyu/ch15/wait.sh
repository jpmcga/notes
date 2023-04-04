#!/bin/bash

while
	[ ! -s $1 ]
do
	echo waiting ...
	sleep 10
	echo ...
	sleep 10
	echo ...
done

echo Data added!

#!/bin/bash

i=0
while
	[ $i -lt 20 ]
do
	i=`expr $i + 1`
	echo $i
done

#!/bin/bash

echo What do you want:
read var
case $var in
house) echo expensive;;
car) echo medium;;
popsicle) echo cheap;;
*) echo idk;;
esac

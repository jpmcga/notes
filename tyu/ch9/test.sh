#!/bin/zsh

cat $* |\
	awk '{for (i=1;i<=NF;i++) print $i}' |\
	fgrep -i -f words 

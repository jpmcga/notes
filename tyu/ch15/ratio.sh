#!/bin/zsh

echo "Number of readers: "
read readers

echo "Number of subscribers: "
read subs

awk "BEGIN { print  $readers/$subs}"

#!/bin/bash

grep -c $2 *.$1 | awk '{print $1}' | tr ":" " " | awk '{print $2}' | sort -r | awk 'FNR <= 3' | awk 'BEGIN {FS="\n"; x=0} {x+=$1} END {print x}'

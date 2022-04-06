#!/bin/bash
echo 'CSC 466 Quiz1, Nicholas Wachter'

#echo 'The corpus has '
tr ' ' '\n' < $1 | sort | uniq -c | wc -l | awk '{printf "The corpus has "$N" uniqe words and " }'
awk '{for(i=1;i<=NF;i++) wCount[$i]++} END {for(word in wCount) if (wCount[word] == 1) print word}' $1 | wc -l | awk '{printf $N}'
echo ' hapax legomena'
echo 'The list of hapax legomena:'
awk '{for(i=1;i<=NF;i++) wCount[$i]++} END {for(word in wCount) if (wCount[word] == 1) print word}' $1 | sort

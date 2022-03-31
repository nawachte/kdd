#!/bin/bash

cut -d ',' -f 2,3,8 uscities.csv | awk -F ',' '{if (($2 == "Alabama") && ($3 >= 1500))  print $1}' | sort | uniq | wc -l | awk '{print "There are "$N" counties that match the criteria."}'

echo -n "The list is: "
cut -d ',' -f 2,3,8 uscities.csv | awk -F ',' '{if (($2 == "Alabama") && ($3 >= 1500) && (substr($1,0,1) != "B")) print $1}'| sort | uniq | tr "\n" "\|"
echo ""

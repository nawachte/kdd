#!/bin/bash

cut -d ',' -f 1,2 1000i.csv | awk -F ',' '{if (($1 >= 600 && $1 <= 900) || $2 == 3) print $2" "$N}' | sort -n | awk '{print $2}' | cut -d ',' -f 1 | sort -n | uniq | wc -l | awk '{print $N" unique numbers here"}'


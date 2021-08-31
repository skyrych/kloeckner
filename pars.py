#!/usr/bin/python3.9
# You run this script providing the name of a log file. For example, ./pars.py --log-file=cri-o.log

import sys
import os

path = sys.argv[1]
file_name = path.split("=")

read = open(file_name[1])
lines = read.readlines()
output = open("parsed_log.log", "w")

for line in lines:
    lst=(line.split(" "))
    print('{' + '\n' + '\t' + '"@timestamp": ' + lst[0] + ',' + '\n' + '\t' + '"stream": ' + lst[1] + ',' + '\n' + '\t' + '"log": ' + ' '.join(map(str, lst[16:-1])) + '\n' + '}', file = output)

read.close()
output.close()

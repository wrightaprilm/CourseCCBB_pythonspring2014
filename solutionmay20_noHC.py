#!/usr/bin/env python 

import sys

input_file = sys.argv[1]

def function_one(file):
	f=open(file,'r')
    return f

def function_two():
    f = function_one()
    line_list = []
    for line in f:     
		line_list.append((line).strip().split(','))
    return line_list

def function_three():
    line_obj = function_two()
    with open('out.txt', 'w') as out_file:
        for line in line_obj:
            out_file.write(str(line) + '\n')

function_three()

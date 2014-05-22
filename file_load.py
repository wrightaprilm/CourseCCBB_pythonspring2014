#!/usr/bin/env python 
import os
def get_files():
    file_list = []
    for file in os.listdir('.'):
        if file.endswith('.csv'):
	    file_list.append(file)
    print file_list
    return(file_list)

if __name__ == '__main__':
    get_files()



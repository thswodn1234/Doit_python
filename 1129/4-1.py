# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:14:47 2022

@author: user
"""

import csv

f = open("test.csv", "r")

new = csv.reader(f)

a_list = []

for line in new:
    a_list.append(line)
    
    
print(a_list)


# 함수로 만들기

def open_csv(file_name):
    f = open(file_name,"r")
    new = csv.reader(f)
    
    a_list = []
    
    for line in new:
        a_list.append(line)
    
    f.close()
    return a_list

li = open_csv('example2.csv')
print(li)



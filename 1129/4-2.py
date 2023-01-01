# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:35:28 2022

@author: user
"""

import csv

def open_csv(file_name):
    f = open(file_name,"r")
    new = csv.reader(f)
    
    a_list = []
    
    for line in new:
        a_list.append(line)
    
    f.close()
    return a_list

def writecsv(filename, the_list):
    f = open(filename,"w",newline="")
    csvobject = csv.writer(f,delimiter=",")
    csvobject.writerows(the_list)
    f.close()
    
li = open_csv('example2.csv')
print(li)


    
data = [['이름', '국어', '영어', '수학'], ['a', '90', '80', '100'], ['b', '80', '90', '90'], ['c', '100', '80', '60']]

writecsv("test3.csv", data)
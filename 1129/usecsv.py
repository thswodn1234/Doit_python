# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:04:54 2022

@author: user
"""
import csv,re

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

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(",","", j))
            except:
                    pass
    return listName

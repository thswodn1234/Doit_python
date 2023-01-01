# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:25:04 2022

@author: user
"""

import usecsv


total = usecsv.open_csv("popSeoul.csv")


for i in total[:5]:
    print(i)
    
import re
for i in total:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(",","",j))
        except:
            pass
total
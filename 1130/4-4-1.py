# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:57:57 2022

@author: user
"""

import usecsv
import re

apt = usecsv.open_csv("apt_202211.csv")
apt = usecsv.switch(apt)

new = [["시군구","전용면적","거래금액","단지명"]]

#for i in apt[:4]:
#    print(i)
    
for i in apt:
    try:
        if i[5]>80 and i[8]>0 and re.search(r'명지',i[0]):
            new.append([i[0], i[5] ,i[8], i[4]])
    except:
        pass

usecsv.writecsv("aptover80_Upper0.csv", new)
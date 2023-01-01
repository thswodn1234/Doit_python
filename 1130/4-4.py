# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:15:14 2022

@author: user
"""
import usecsv

pop = usecsv.open_csv("popSeoul.csv")
print(pop[:4])


pop = usecsv.switch(pop)


#for i in pop:
#    try:
#        f = round(i[2]/(i[1] + i[2])*100,1)
#        print(f"구이름 : {i[0]} 외국인 비율{f}")
#    except:
#        pass
    
new = [["구", "한국인수", "외국인수", "외국인 비율(%)"]]
for i in pop:
    try:
        f = round(i[2]/(i[1] + i[2])*100,1)
        if f>3:
            new.append([i[0],i[1], i[2],f])
    except:
        pass
    
usecsv.writecsv("newPop.csv", new)
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:49:28 2022

@author: user
"""

import re

f = open('friends101.txt', 'r')
s101 = f.read()
f.close()

#Monica = re.findall(r"Monica:.+", s101)

# a = [i for i in Monica]

# for i in range(0,len(a)):
#    print(a[i])

#for line in Monica:
 #   print(line)

# 개행 없이 다 더해서 저장
#Mon = ""
#for line in Monica:
#    Mon = Mon +  line

#print(Mon)

#Mon = ""
#for line in Monica:
 #   Mon = Mon +  line+"\n"

#f = open("Monica.txt","w")
#f.write(Mon)
#f.close()

# 등장인물 이름

#char = re.findall(r"[A-Z][a-z]{1,7}:", s101)

#ch = []
#for c in list(set(char)):
#    print(re.sub(r':','',c))
# 리스트 추가
#    ch.append(re.sub(r':','',c))
# 위와 동일
# ch += [re.sub(r':','',c)]
#print(ch)

#would 찾기

f = open('friends101.txt','r')
s101 = f.readlines()
f.close()

would=[]

for line in s101:
    if re.match(r'[A-Z][a-z]+.:',line) and re.search(r'would', line):
        would.append(line)

for line in would:
    print(line)
    
    
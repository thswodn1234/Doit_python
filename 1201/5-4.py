# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:34:44 2022

@author: user
"""

import pandas as pd
data = {'name':['Mark','Jane','Chris','Ryan'],
        'age':[33,32,44,42],
        'score':[91.3, 83.4, 77.5, 87.7]}
df = pd.DataFrame(data)
print(df)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:23:59 2022

@author: user
"""

import numpy as np
discount = .05
cashflow = 100

def presentvalue(n):
  return (cashflow/((1+discount)**n))

print(presentvalue(1))
print(presentvalue(2))

for i in range(20):
  print(presentvalue(i))
  
  loss = [-750, -250]
profit = [100]*18
cf = loss+profit
print()

cashflow = np.array(cf)


import numpy_financial as npf

npv = npf.npv(0.045, cashflow)
print(f"npv: {npv}")
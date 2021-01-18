# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:50:46 2020

@author: 105961
"""

from mypulp import *

a = {(1,1):.25, (1,2):.15, (1,3):.3,
     (2,1):.3,  (2,2):.3,  (2,3):.1,
     (3,1):.15, (3,2):.65, (3,3):.05,
     (4,1):.1,  (4,2):.05, (4,3):.85,
    }
I = [1, 2, 3, 4]
p = {1:5, 2:6, 3:8, 4:20}
K = [1, 2, 3]
LB = {1:.1, 2:.0, 3:.45}
UB = {1:.2, 2:.35, 3:1.0}

#モデルの定義
model = Model(name = "product mix")
#変数の定義
x = {}

for i in I:
    x[i] = model.addVar()
model.update()
model.addConstr(quicksum(x[i] for i in I)==1)
for k in K:
    model.addConstr(quicksum(a[i,k]*x[i] for i in I)<=UB[k])
    model.addConstr(quicksum(a[i,k]*x[i] for i in I)>=LB[k])
#目的関数
model.setObjective(quicksum(p[i]*x[i] for i in I),GRB.MINIMIZE)
model.optimize()
for i in I:
    print(i,x[i].X)
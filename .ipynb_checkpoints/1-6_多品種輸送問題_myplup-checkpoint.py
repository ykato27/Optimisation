# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:00:53 2020

@author: 105961
"""

from mypulp import *

produce = {1:[2,4], 2:[1,2,3], 3:[2,3,4]}
d = {(1,1):80,   (1,2):85,   (1,3):300, (1,4):6,
     (2,1):270,  (2,2):160,  (2,3):400, (2,4):7,
     (3,1):250,  (3,2):130,  (3,3):350, (3,4):4,
     (4,1):160,  (4,2):60,   (4,3):200, (4,4):3,
     (5,1):180,  (5,2):40,   (5,3):150, (5,4):5
    }
I = set([i for (i,k) in d])
J = [1, 2, 3]
M = {1:3000, 2:3000, 3:3000}
K = [1, 2, 3, 4]
weight = {1:5, 2:2, 3:3, 4:4}
cost = {(1,1):4,  (1,2):6,  (1,3):9,
        (2,1):5,  (2,2):4,  (2,3):7,
        (3,1):6,  (3,2):3,  (3,3):4,
        (4,1):8,  (4,2):5,  (4,3):3,
        (5,1):10, (5,2):8,  (5,3):4,
       }

c = {}
for i in I:
    for j in J:
        for k in produce[j]:
            c[i, j, k] = cost[i, j] * weight[k]

#モデルの定義
model = Model(name = "multi-commodity transportation")
#変数の定義
x = {}
for i,j,k in c:
    x[i,j,k] = model.addVar(vtype="C")
model.update()

for i in I:
    for k in K:
        model.addConstr(quicksum(x[i,j,k] for j in J if (i,j,k) in x)==d[i,k])

for j in J:
    model.addConstr(quicksum(x[i,j,k] for (i,j2,k) in x if j2 == j) <= M[j])
    
#目的関数
model.setObjective(quicksum(c[i,j,k]*x[i,j,k] for (i,j,k) in x), GRB.MINIMIZE)

model.optimize()
print("Opt value:", model.ObjVal)
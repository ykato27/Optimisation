# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 08:14:06 2020

@author: 105961
"""

from mypulp import *

d = {1:80, 2:270, 3:250, 4:160, 5:180}
M = {1:500, 2:500, 3:500}
I = [1, 2, 3, 4, 5]
J = [1, 2, 3]
c = {(1,1):4,  (1,2):6,  (1,3):9,
     (2,1):5,  (2,2):4,  (2,3):7,
     (3,1):6,  (3,2):3,  (3,3):4,
     (4,1):8,  (4,2):5,  (4,3):3,
     (5,1):10, (5,2):8,  (5,3):4,
    }

#モデルの定義
model = Model("transportation")
#変数の定義
x = {}
for i in I:
    for j in J:
        x[i,j] = model.addVar(vtype="C", name="x(%s,%s)" %(i,j))
model.update()

for i in I:
    model.addConstr(quicksum(x[i,j] for j in J)==d[i], name="Demand(%s)" %i)
for j in J:
    model.addConstr(quicksum(x[i,j] for i in I) <=M[j], name="Capacity(%s)" %j)
model.setObjective(quicksum(c[i,j]*x[i,j] for (i,j) in x),GRB.MINIMIZE)

model.optimize()
print ("Opt.value:", model.ObjVal)
EPS = 1.e-6
for (i,j) in x:
    if x[i,j].X > EPS:
        print ("sending quantity %10s from factory %3s to ccustomer %3s" % (x[i,j].X, j, i))
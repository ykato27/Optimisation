# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:24:36 2020

@author: 105961
"""

from mypulp import *

def CuttingStockExample():
    B = 9
    w = [2,3,4,5,6,7,8]
    q = [4,2,6,6,2,2,2]
    s = []
    for j in range(len(w)):
        for i in range(q[j]):
            s.append(w[j])
    return s, B

def FFD(s, B):
    remain = [B]
    sol = [[]]
    for item in sorted(s, reverse = True):
        for (j, free) in enumerate(remain):
            if free >= item:
                remain[j] -= item
                sol[j].append(item)
                break
        else:
            sol.append([item])
            remain.append(B-item)
    return sol

def bpp(s, B):
    n = len(s)
    U = len(FFD(s,B))
    model = Model("bpp")
    x, y = {}, {}
    for i in range(n):
        for j in range(U):
            x[i,j] = model.addVar(vtype="B")
    for j in range(U):
        y[j] = model.addVar(vtype="B")
    model.update()
    
    for i in range(n):
        model.addConstr(quicksum(x[i,j] for j in range(U))==1)
    for j in range(U):
        model.addConstr(quicksum(s[i]*x[i,j] for i in range(n)) <= B*y[j])
    for j in range(U):
        for i in range(n):
            model.addConstr(x[i,j] <= y[j])
    model.setObjective(quicksum(y[j] for j in range(U)), GRB.MINIMIZE)
    model.update
    model.__data = x, y
    return model

if __name__ == "__main__":
    s, B = CuttingStockExample()
    sol = FFD(s, B)
    model = bpp(s, B)
    model.optimize()
    print("Opt Value=", model.ObjVal)
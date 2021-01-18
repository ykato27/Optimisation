# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:13:40 2020

@author: 105961
"""

import random
from mypulp import *

def make_data(n,m):
    """make_data: prepare matrix of m times n random processing times"""
    p = {}
    for i in range(1,m+1):
        for j in range(1,n+1):
            p[i,j] = random.randint(1,10)
    return p


def example():
    proc = [[2,3,1],[4,2,3],[1,4,1]]
    p = {}
    for i in range(3):
        for j in range(3):
            p[i+1,j+1] = proc[j][i]
    return p

def permutation_flow_shop(n,m,p):
    model = Model("permutation flow shop")
    x,s,f = {},{},{}
    for j in range(1, n+1):
        for k in range(1, n+1):
            x[j,k] = model.addVar(vtype="B")
    for i in range(1, m+1):
        for k in range(1, n+1):
            s[i,k] = model.addVar(vtype="C")
            f[i,k] = model.addVar(vtype="C")
    model.update()
    
    for j in range(1, n+1):
        model.addConstr(quicksum(x[j,k] for k in range(1,n+1)) == 1)
        model.addConstr(quicksum(x[k,j] for k in range(1,n+1)) == 1)
    for i in range(1, m+1):
        for k in range(1, n+1):
            if k != n:
                model.addConstr(f[i,k] <= s[i,k+1])
            if i != m:
                model.addConstr(f[i,k] <= s[i+1,k])
            model.addConstr(s[i,k] + quicksum(p[i,j]*x[j,k] for j in range(1,n+1)) <= f[i,k])
    model.setObjective(f[m,n], GRB.MINIMIZE)
    model.update()
    model.__data = x,s,f
    return model

if __name__ == "__main__":
    random.seed(1)
    n = 15
    m = 10
    p = make_data(n,m)
    model = permutation_flow_shop(n, m, p)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
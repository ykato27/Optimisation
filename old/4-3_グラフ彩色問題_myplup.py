# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:18:38 2020

@author: 105961
"""

from mypulp import *
import random

def make_data(n, prob):
    V = range(1,n+1)
    E = [(i,j) for i in V for j in V if i < j and random.random() < prob]
    return V, E

def gcp(V,E,K):
    model = Model(name="gcp")
    x, y = {}, {}
    for k in range(K):
        y[k] = model.addVar(vtype="B")
        for i in V:
            x[i,k] = model.addVar(vtype="B")
    model.update()
    
    for i in V:
        model.addConstr(quicksum(x[i,k] for k in range(K))==1)
    for (i,j) in E:
        for k in range(K):
            model.addConstr(x[i,k] + x[j,k]<=y[k])
    for k in range(K-1):
        model.addConstr(y[k] >= y[k+1])
    model.setObjective(quicksum(y[k] for k in range(K)), GRB.MINIMIZE)
    model.update()
    model.__data = x
    return model

if __name__ == "__main__":
    V, E = make_data(10,.5)
    model = gcp(V,E,K)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
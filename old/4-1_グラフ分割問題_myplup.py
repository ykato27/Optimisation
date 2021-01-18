# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 07:25:18 2020

@author: 105961
"""

from mypulp import *
import random

def make_data(n, prob):
    V = range(1,n+1)
    E = [(i,j) for i in V for j in V if i < j and random.random() < prob]
    return V, E

def gpp(V, E):
    model = Model(name="gpp")
    x, y = {}, {}
    for i in V:
        x[i] = model.addVar(vtype="B")
    for (i,j) in E:
        y[i,j] = model.addVar(vtype="B")
    model.update()
    
    model.addConstr(quicksum(x[i] for i in V)==len(V)/2)
    for (i,j) in E:
        model.addConstr(x[i] - x[j] <= y[i,j])
        model.addConstr(x[j] - x[i] <= y[i,j])
    
    model.setObjective(quicksum(y[i,j] for (i,j) in E), GRB.MINIMIZE)
    model.update()
    model.__data = x
    return model

if __name__ == "__main__":
    V, E = make_data(10,.5)
    model = gpp(V,E)
    model.optimize()
    print ("Opt.Value-",model.ObjVal)
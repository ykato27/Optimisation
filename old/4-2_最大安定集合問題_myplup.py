# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 07:52:53 2020

@author: 105961
"""

from mypulp import *
import random

def make_data(n, prob):
    V = range(1,n+1)
    E = [(i,j) for i in V for j in V if i < j and random.random() < prob]
    return V, E

def ssp(V,E):
    model = Model(name="ssp")
    x = {}
    for i in V:
        x[i] = model.addVar(vtype="B")
    model.update()
    
    for(i,j) in E:
        model.addConstr(x[i] + x[j] <= 1)
    
    model.setObjective(quicksum(x[i] for i in V), GRB.MAXIMIZE)
    model.update()
    model.__data = x
    return model

if __name__ == "__main__":
    V, E = make_data(10,.5)
    model = ssp(V,E)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
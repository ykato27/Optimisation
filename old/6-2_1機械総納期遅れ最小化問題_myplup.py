# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 07:42:48 2020

@author: 105961
"""

from mypulp import *

def make_data():
    J = {1,2,3,4,5,6}
    p = {1:1,2:4,3:2,4:3,5:1,6:4}
    r = {1:4,2:0,3:2,4:4,5:1,6:5}
    w = {1:3,2:1,3:2,4:3,5:1,6:2}
    return J, p, r, w

def scheduling_linear_ordering(J,p,d,w):
    model = Model("scheduling: linear ordering")
    T,x = {},{}
    for j in J:
        T[j] = model.addVar(vtype="C")
        for k in J:
            if j != k:
                x[j,k] = model.addVar(vtype="B")
    model.update()
    
    for j in J:
        model.addConstr(quicksum(p[k]*x[k,j] for k in J if k!=j)-T[j] <= d[j]-p[j])
        for k in J:
            if k <= j:
                continue
            model.addConstr(x[j,k] + x[k,j] == 1)
            for ell in J:
                if ell > k:
                    model.addConstr(x[j,k] + x[k,ell] + x[ell,j] <= 2)
                    
    model.setObjective(quicksum(w[j]*T[j] for j in J), GRB.MINIMIZE)
    model.update()
    model.__data = x,T
    return model

if __name__ == "__main__":
    J, p, r, w = make_data()
    model = scheduling_linear_ordering(J, p, r, w)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
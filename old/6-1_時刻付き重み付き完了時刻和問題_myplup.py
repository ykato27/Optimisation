# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:30:46 2020

@author: 105961
"""

from mypulp import *

def make_data():
    J = {1,2,3,4,5,6}
    p = {1:1,2:4,3:2,4:3,5:1,6:4}
    r = {1:4,2:0,3:2,4:4,5:1,6:5}
    w = {1:3,2:1,3:2,4:3,5:1,6:2}
    return J, p, r, w

def scjeduling_disjunctive(J, p, r, w):
    model = Model(name="schedulin: disjunctive")
    # big M
    M = max(r.values()) + sum(p.values())
    s, x = {}, {}
    for j in J:
        for k in J:
            if j != k:
                x[j,k] = model.addVar(vtype="B", name="x(%s,%s)"%(j,k))
    model.update()

    for j in J:
        model.addConstr(s[j] >= r[j])
        for k in J:
            if j != k:
                model.addConstr(s[j] - s[k] + M*x[j,k] <= (M-p[j]))
            if j < k:
                model.addConstr(x[j, k] + x[k, j] == 1)
    model.setObjective(quicksum(w[j]*s[j] for j in J), GRB.MINIMIZE)
    model.update()
    model.__data = s,x
    return model

if __name__ == "__main__":
    J, p, r, w = make_data()
    model = scjeduling_disjunctive(J, p, r, w)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
            
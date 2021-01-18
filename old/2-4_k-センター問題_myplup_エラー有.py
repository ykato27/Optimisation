# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:38:04 2020

@author: 105961
"""

from mypulp import *

def make_data():
    I, d = multidict({1:80, 2:270, 3:250, 4:160, 5:180})
    J, M, f = multidict({1:[500,1000], 2:[500,1000], 3:[500,1000]})
    c = {(1, 1):4,  (1, 2):6,  (1, 3):9,
         (2, 1):5,  (2, 2):4,  (2, 3):7,
         (3, 1):6,  (3, 2):3,  (3, 3):4,
         (4, 1):8,  (4, 2):5,  (4, 3):3,
         (5, 1):10, (5, 2):8,  (5, 3):4,
        }
    return I, J, d, M, f, c

def kcenter(I, J, c, k):
    model = Model(name="k-center")
    z = model.addVar(vtype="C")
    x, y = {}, {}
    for j in J:
        y[j] = model.addVar(vtype="B")
        for i in I:
            x[i,j] = model.addVar(vtype="B")
    model.update()
    
    for i in I:
        model.addConstr(quicksum(x[i,j] for j in J)==1)
        model.addConstr(quicksum(c[i,j]*x[i,j] for j in J)<=z,"MAX_x(%s)"%(i))
        for j in J:
            model.addConstr(x[i,j] <= y[j])
    
    model.addConstr(quicksum(y[j] for j in J)==k)
    model.setObjectie(z, GRB.MINIMIZE)
    model.update()
    model.__data = x,y
    return model

if __name__ == "__main__":
    I, J, d, c, f, M = make_data()
    k = 1
    model = kcenter(I, J, c, k)
    model.optimize()
    print("Opt Value=", model.ObjVal)
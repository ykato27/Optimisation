# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:42:01 2020

@author: 105961
"""

import random
from mypulp import *

def make_data_10():
    """
    1..T: set of periods
    K: set of resources
    P: set of items
    f[t,p]: set-up costs
    g[t,p]: set-up times
    c[t,p]: variable costs
    d[t,p]: demand values
    h[t,p]: holding costs
    a[t,k,p]: amount of resource k for producing product p in period. t
    M[t,k]: resource upper bounds
    UB[t,p]: upper bound of production time of product p in period t
    phi[(i,j)] : units of i required to produce a unit of j (j parent of i)
    """
    T = 5
    K = [1]
    P = [1,2,3,4,5,6,7,8,9,10]
    _, f, g, c, d, h, UB = multidict({
        (1,1): [10, 1, 2,  0, 0.5, 24],
        (1,2): [10, 1, 2,  0, 0.5, 24],
        (1,3): [10, 1, 2,  0, 0.5, 24],
        (1,4): [10, 1, 2,  0, 0.5, 24],
        (1,5): [10, 1, 2,  0, 0.5, 24],
        (1,6): [10, 1, 2,  0, 0.5, 24],
        (1,7): [10, 1, 2,  0, 0.5, 24],
        (1,8): [10, 1, 2,  0, 0.5, 24],
        (1,9): [10, 1, 2,  0, 0.5, 24],
        (1,10):[10, 1, 2,  0, 0.5, 24],
        (2,1): [10, 1, 2,  0, 0.5, 24],
        (2,2): [10, 1, 2,  0, 0.5, 24],
        (2,3): [10, 1, 2,  0, 0.5, 24],
        (2,4): [10, 1, 2,  0, 0.5, 24],
        (2,5): [10, 1, 2,  0, 0.5, 24],
        (2,6): [10, 1, 2,  0, 0.5, 24],
        (2,7): [10, 1, 2,  0, 0.5, 24],
        (2,8): [10, 1, 2,  0, 0.5, 24],
        (2,9): [10, 1, 2,  0, 0.5, 24],
        (2,10):[10, 1, 2,  0, 0.5, 24],
        (3,1): [10, 1, 2,  0, 0.5, 24],
        (3,2): [10, 1, 2,  0, 0.5, 24],
        (3,3): [10, 1, 2,  0, 0.5, 24],
        (3,4): [10, 1, 2,  0, 0.5, 24],
        (3,5): [10, 1, 2,  0, 0.5, 24],
        (3,6): [10, 1, 2,  0, 0.5, 24],
        (3,7): [10, 1, 2,  0, 0.5, 24],
        (3,8): [10, 1, 2,  0, 0.5, 24],
        (3,9): [10, 1, 2,  0, 0.5, 24],
        (3,10):[10, 1, 2,  0, 0.5, 24],
        (4,1): [10, 1, 2,  0, 0.5, 24],
        (4,2): [10, 1, 2,  0, 0.5, 24],
        (4,3): [10, 1, 2,  0, 0.5, 24],
        (4,4): [10, 1, 2,  0, 0.5, 24],
        (4,5): [10, 1, 2,  0, 0.5, 24],
        (4,6): [10, 1, 2,  0, 0.5, 24],
        (4,7): [10, 1, 2,  0, 0.5, 24],
        (4,8): [10, 1, 2,  0, 0.5, 24],
        (4,9): [10, 1, 2,  0, 0.5, 24],
        (4,10):[10, 1, 2,  0, 0.5, 24],
        (5,1): [10, 1, 2,  0, 0.5, 24],
        (5,2): [10, 1, 2,  0, 0.5, 24],
        (5,3): [10, 1, 2,  0, 0.5, 24],
        (5,4): [10, 1, 2,  0, 0.5, 24],
        (5,5): [10, 1, 2,  0, 0.5, 24],
        (5,6): [10, 1, 2,  0, 0.5, 24],
        (5,7): [10, 1, 2,  0, 0.5, 24],
        (5,8): [10, 1, 2,  0, 0.5, 24],
        (5,9): [10, 1, 2,  0, 0.5, 24],
        (5,10):[10, 1, 2,  5, 0.5, 24],
        })
    a = {
        (1,1,1): 1, (1,1,2): 1, (1,1,3): 1, (1,1,4): 1, (1,1,5): 1, (1,1,6): 1, (1,1,7): 1, (1,1,8): 1, (1,1,9): 1, (1,1,10): 1,
        (2,1,1): 1, (2,1,2): 1, (2,1,3): 1, (2,1,4): 1, (2,1,5): 1, (2,1,6): 1, (2,1,7): 1, (2,1,8): 1, (2,1,9): 1, (2,1,10): 1,
        (3,1,1): 1, (3,1,2): 1, (3,1,3): 1, (3,1,4): 1, (3,1,5): 1, (3,1,6): 1, (3,1,7): 1, (3,1,8): 1, (3,1,9): 1, (3,1,10): 1,
        (4,1,1): 1, (4,1,2): 1, (4,1,3): 1, (4,1,4): 1, (4,1,5): 1, (4,1,6): 1, (4,1,7): 1, (4,1,8): 1, (4,1,9): 1, (4,1,10): 1,
        (5,1,1): 1, (5,1,2): 1, (5,1,3): 1, (5,1,4): 1, (5,1,5): 1, (5,1,6): 1, (5,1,7): 1, (5,1,8): 1, (5,1,9): 1, (5,1,10): 1,
        }
    M = {
        (1,1): 25,
        (2,1): 25,
        (3,1): 25,
        (4,1): 25,
        (5,1): 25,
        (6,1): 25,
        (7,1): 25,
        (8,1): 25,
        (9,1): 25,
        (10,1):25,
        }

    phi = {     # phi[(i,j)] : units of i required to produce a unit of j (j parent of i)
        (1,2):1,
        (2,5):2,
        (3,4):3,
        (4,5):1,
        (5,6):1,
        (6,10):1/2.,
        (3,7):1,
        (7,8):3/2.,
        (8,9):3,
        (9,10):1
        }
    

    return T,K,P,f,g,c,d,h,a,M,UB,phi

def mils_standard(T,K,P,f,g,c,d,h,a,M,UB,phi):

    model = Model("multi-stage lotsizing -- standard formulation")
    y,x,I = {},{},{}
    Ts = range(1,T+1)
    for p in P:
        for t in Ts:
            y[t,p] = model.addVar(vtype="B", name="y(%s,%s)"%(t,p))
            x[t,p] = model.addVar(vtype="C",name="x(%s,%s)"%(t,p))
            I[t,p] = model.addVar(vtype="C",name="I(%s,%s)"%(t,p))
        I[0,p] = model.addVar(name="I(%s,%s)"%(0,p))
    model.update()

    for t in Ts:
        for p in P:
            # flow conservation constraints
            model.addConstr(I[t-1,p] + x[t,p] == \
                            quicksum(phi[p,q]*x[t,q] for (p2,q) in phi if p2 == p) \
                            + I[t,p] + d[t,p],
                            "FlowCons(%s,%s)"%(t,p))

            # capacity connection constraints
            model.addConstr(x[t,p] <= UB[t,p]*y[t,p], "ConstrUB(%s,%s)"%(t,p))

        # time capacity constraints
        for k in K:
            model.addConstr(quicksum(a[t,k,p]*x[t,p] + g[t,p]*y[t,p] for p in P) <= M[t,k],
                            "TimeUB(%s,%s)"%(t,k))

    # initial inventory quantities
    for p in P:
        model.addConstr(I[0,p] == 0, "InventInit(%s)"%(p))

    model.setObjective(\
        quicksum(f[t,p]*y[t,p] + c[t,p]*x[t,p] + h[t,p]*I[t,p] for t in Ts for p in P), \
        GRB.MINIMIZE)

    model.update()
    model.__data = y,x,I
    return model

if __name__ == "__main__":
    T,K,P,f,g,c,d,h,a,M,UB,phi = make_data_10()
    model = mils_standard(T,K,P,f,g,c,d,h,a,M,UB,phi)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)

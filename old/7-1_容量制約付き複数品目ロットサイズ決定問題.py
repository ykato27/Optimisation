# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:11:35 2020

@author: 105961
"""

import random
from mypulp import *

def trigeiro(T,N,factor):

    P = range(1,N+1)
    f,g,c,d,h,M = {},{},{},{},{},{}

    sumT = 0
    for t in range(1,T+1):
        for p in P:
            g[t,p] = 10 * random.randint(1,5)   # 10, 50: trigeiro's values

            f[t,p] = 100 * random.randint(1,10) # checked from Wolsey's instances
            c[t,p] = 0                          # variable costs

            d[t,p] = 100+random.randint(-25,25) # checked from Wolsey's instances
            if t <= 4:
                if random.random() < .25:       # trigeiro's parameter
                    d[t,p] = 0
            sumT += g[t,p] + d[t,p]             # sumT is the total capacity usage in the lot-for-lot solution
            h[t,p] = random.randint(1,5)        # holding costs; checked from Wolsey's instances

    for t in range(1,T+1):
        M[t] = int(float(sumT)/float(T)/factor)

    return P,f,g,c,d,h,M

def mils(T,P,f,g,c,d,h,M):
    model = Model(name = "standard multi-item lotsizing")
    y,x,I = {},{},{}
    Ts = range(1,T+1)
    for p in P:
        for t in Ts:
            y[t,p] = model.addVar(vtype="B")
            x[t,p] = model.addVar(vtype="C")
            I[t,p] = model.addVar(vtype="C")
        I[0,p] = 0
    model.update()
    
    for t in Ts:
        model.addConstr(quicksum(g[t,p]*y[t,p]+x[t,p] for p in P) <= M[t])
        for p in P:
            model.addConstr(I[t-1,p] + x[t,p] == I[t,p] + d[t,p])
            model.addConstr(x[t,p] <= (M[t]-g[t,p])*y[t,p])
    model.setObjective(quicksum(f[t,p]*y[t,p]+c[t,p]*x[t,p]+h[t,p]*I[t,p] for t in Ts for p in P),GRB.MINIMIZE)
    model.update()
    model.__data = y,x,I
    return model

if __name__ == "__main__":
    T,N,factor = 15,6,0.75
    P,f,g,c,d,h,M = trigeiro(T,N,factor)
    model = mils(T,P,f,g,c,d,h,M)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
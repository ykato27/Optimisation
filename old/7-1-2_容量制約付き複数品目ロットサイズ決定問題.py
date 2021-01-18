# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:40:29 2020

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

def mils_fl(T,P,f,g,c,d,h,M):
    Ts = range(1,T+1)
    model = Model(name="multi-item lotsizing -- facility location formulation")
    y,X = {},{}
    for p in P:
        for t in Ts:
            y[t,p] = model.addVar(vtype="B")
            for s in range(1,t+1):
                X[s,t,p] = model.addVar(vtype="C")
    model.update()
    
    for t in Ts:
        model.addConstr(quicksum(X[t,s,p] for s in range(t,T+1) for p in P)+quicksum(g[t,p]*y[t,p] for p in P) <= M[t])
        for p in P:
            model.addConstr(quicksum(X[s,t,p] for s in range(1,t+1)) == d[t,p])
            for s in range(1,t+1):
                model.addConstr(X[s,t,p] <= d[t,p] * y[s,p])
    C = {}
    for p in P:
        for s in Ts:
            sumC = 0
            for t in range(s,T+1):
                C[s,t,p] = (c[s,p]+sumC)
                sumC += h[t,p]
    model.setObjective(quicksum(f[t,p]*y[t,p] for t in Ts for p in P)+
                       quicksum(C[s,t,p]*X[s,t,p] for t in Ts for p in P for s in range(1,t+1)),GRB.MINIMIZE)
    model.update()
    model.__data = y,X
    return model

if __name__ == "__main__":
    T,N,factor = 15,6,0.75
    P,f,g,c,d,h,M = trigeiro(T,N,factor)
    model = mils_fl(T,P,f,g,c,d,h,M)
    model.optimize()
    print ("Opt.Value=",model.ObjVal)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:39:04 2020

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

def mils_callback(model, where):
    if where != GRB.Callback.MIPSOL and where != GRB.Callback.MIPNODE:
        return
    for p in P:
        for ell in Ts:
            lhs = 0
            S,L = [],[]
            for t in range(l,ell+1):
                yt = model.cbGetSolution(y[t,p])
                xt = model.cbGetSolution(x[t,p])
                if D[t,ell,p]*yt < xt:
                    S.append(t)
                    lhs += D[t,ell,p]*yt
                else:
                    L.append(t)
                    lhs += xt
            if lhs < D[1,ell,p]:
                model.cbLazy(quicksum(x[t,p] for t in L) + quicksum(D[t,ell,p]*y[t,p] for t in S) >= D[1,ell,p])
    return


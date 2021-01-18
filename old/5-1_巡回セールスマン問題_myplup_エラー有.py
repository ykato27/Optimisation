# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:20:23 2020

@author: 105961
"""

from mypulp import *
import random
import networkx
import math
import time

def make_data(n):
    """make_data: compute matrix distance based on euclidean distance"""
    V = range(1,n+1)
    x = dict([(i,random.random()) for i in V])
    y = dict([(i,random.random()) for i in V])
    c = {}
    for i in V:
        for j in V:
            if j > i:
                c[i,j] = distance(x[i],y[i],x[j],y[j])
    return V,c

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def addcut(edges):
    G = networkx.Graph()
    G.add_nodes_from(V)
    for (i,j) in edges:
        G.add_edge(i,j)
    Components = networkx.connected_components(G)
    if len(Components)==1:
        return False
    for S in Components:
        model.addConstr(qucksum(x[i,j] for i in S for j in S if j>i) < len(S)-1)
    return True

def solve_tsp(V,c):
    model = Model(name="tsp")
    x = {}
    for i in V:
        for j in V:
            if j > i:
                x[i,j] = model.addVar(ub=1, name="x(%s,%s)"%(i,j))
    model.update()
    
    for i in V:
        model.addConstr(quicksum(x[i,j] for j in V if j < i) + quicksum(x[i,j] for j in V if j > i)==2)
    
    model.ssetObjective(quicksum(c[i,j]*x[i,j] for i in V for j in V if j > i), GRB.MINIMIZE)
    EPS = 1.e-6
    while True:
        model.optimize()
        edges = []
        for (i,j) in x:
            if x[i,j].X > EPS:
                edges.append((i,j))
        if addcut(edges) == False:
            if model.IsMIP:
                break
            for (i,j) in x:
                x[i,j].Vtype = "B"
            model.update()
    return model.ObjVal, edges



if __name__ == "__main__":
    V, c = make_data(20)
    obj,edges = solve_tsp(V,c)
    model.optimize()
    print ("Opt.tour=",edges)
    print ("Opt.cost=",obj)
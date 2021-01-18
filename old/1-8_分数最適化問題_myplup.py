# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:17:56 2020

@author: 105961
"""

from mypulp import *

model = Model(name="fractional 1")
#変数定義
x = model.addVar()
y = model.addVar()
z = model.addVar()
t = model.addVar()
model.update()
#制約条件
model.addConstr(x+y+z==32*t)
model.addConstr(2*x+4*y+8*z==80*t)
model.addConstr(2*x+4*y==1)
#目的関数
model.setObjective(x+y, GRB.MINIMIZE)
model.optimize()

print("Opt. Val=", model.ObjVal,", t=",t.X)
print("(x,y,z)=", x.X/t.X, y.X/t.X, z.X/t.X)
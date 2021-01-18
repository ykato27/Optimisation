# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 06:57:01 2020

@author: 105961
"""

from mypulp import *

model = Model("puzzle")
x = model.addVar(name = "x", vtype="I")
y = model.addVar(name = "y", vtype="I")
z = model.addVar(name = "z", vtype="I")
model.update()
model.addConstr(x + y + z == 32)
model.addConstr(2*x + 4*y +8*z == 80)
model.setObjective(y + z, GRB.MINIMIZE)
model.optimize()
print("Opt.Value = ",model.ObjVal)
for i in model.getVars():
    print(i.VarName, i.X)
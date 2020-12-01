#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importsys
# !{sys.executable} -m pip install ortools 

import pandas as pd
import numpy as np
import time
from ortools.sat.python import cp_model


# In[2]:


StartTime = time.process_time()

Happy = cp_model.CpModel()


# Define our variables: there are 15 students, 5 groups, 7 days

Students = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Groups = [1,2,3,4,5]
Days = [1,2,3,4,5,6,7]


# Define the boolean variable X[s,g,d], which equals 1 if student s 
# works in group g on day d, and is equal to 0 otherwise.

X = {}
for s in Students:
    for g in Groups:
        for d in Days:
            X[s,g,d] = Happy.NewIntVar(0, 1, 'X[%d,%d,%d]'%(s,g,d))
        
        
# Constraint 1: each student is assigned to one group
# TO BE ADDED


# Constraint 2: each group has exactly three students
# TO BE ADDED


# Constraint 3: students i and j must be in the same group exactly once
# Alternatively, this constraint is identical to the following:
# "students i and j cannot be in the same group more than once"
# This is because there are n=15 students and d = (n-1)/2 = 7 days.
#
# TO BE ADDED


    
solver = cp_model.CpSolver()
status = solver.Solve(Happy)
                
totalTime = time.process_time() - StartTime
print("Total Time was", totalTime, "seconds")
print("")

if status == cp_model.FEASIBLE:
    print("We found a solution")
    for d in Days:
        for g in Groups:
            for s in Students:
                if solver.Value(X[s,g,d])==1:
                    print("Day", d, "Group", g, "Student", s)
                


# In[ ]:





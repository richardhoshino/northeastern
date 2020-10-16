#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import sys
# !{sys.executable} -m pip install ortools 

import pandas as pd
import numpy as np
import time
from ortools.linear_solver import pywraplp


# In[2]:


InputData = pd.read_excel("United Way Data.xlsx")
InputData


# In[3]:


# Determine the start time
StartTime = time.process_time()

# Define our Integer Linear Program
Solver = pywraplp.Solver('Solver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Define the Happiness coefficient H[i,j], for Employee i working on Month j
H = np.zeros(shape=(6,9), dtype=int)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
for j in range(9):
    for i in range(6):
        H[i,j] = InputData[months[j]][i]
        
# Define the binary variable X[i,j], which will equal 1 if 
# Employee i is assigned to Month j
X = {}
for i in range(6):
    for j in range(9):
        X[i,j] = Solver.IntVar(0, 1, 'X[%d, %d]' % (i,j))
        
# Set up our Happiness Function, which maximizes the total number of Happiness Points
HappinessFunction = Solver.Sum(H[i,j]*X[i,j] for i in range(6) for j in range(9))
Solver.Maximize(HappinessFunction)

# Include our first constraint: Each Employee must work 3 Months
for i in range(6):
    Solver.Add(Solver.Sum([X[i,j] for j in range(9)]) == 3)
                       
# Include our second constraint: Each Month must be covered by 2 Employees
for j in range(9):
    Solver.Add(Solver.Sum([X[i,j] for i in range(6)]) == 2)

# Solve the Integer Linear program
Output = Solver.Solve()
TotalPoints = round(Solver.Objective().Value())

# Determine the total time of running Solver
TotalTime = round(time.process_time() - StartTime, 5)

# Output one of the possible optimal solutions.
print("Python returns a solution with", TotalPoints, 
      "Total Happiness Points in", TotalTime, "seconds")


# In[4]:


pd.options.mode.chained_assignment = None
OutputData = InputData.copy()
for i in range(6):
    for j in range(9):
        if X[i,j].solution_value()==0:
            OutputData[months[j]][i] = ""
OutputData 


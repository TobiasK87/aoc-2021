# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:11:27 2021

@author: Tobi
"""

import math
import pandas as pd
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day4_Input.csv", sep=';')

#############################################################################################
# Problem 1
#############################################################################################

input = [13,79,74,35,76,12,43,71,87,72,23,91,31,67,58,61,96,16,81,92,41,6,32,86,77,42,0,55,68,14,53,26,25,11,45,94,75,1,93,83,52,7,4,22,34,64,69,88,65,66,39,97,27,29,78,5,49,82,54,46,51,28,98,36,48,15,2,50,38,24,89,59,8,3,18,47,10,90,21,80,73,33,85,62,19,37,57,95,60,20,99,17,63,56,84,44,40,70,9,30]
zeros = [0]*df.shape[0]
df_called = pd.DataFrame({'A':zeros, 'B':zeros, 'C':zeros, 'D':zeros, 'E':zeros})#, B=0, C=0, D=0, E=0)

df['Group'] = sum([[i]*5 + [0] for i in range(1,101)], [])[:-1]
df_called['Group'] = sum([[i]*5 + [0] for i in range(1,101)], [])[:-1]


for m in range(df.shape[0]):
    for n in range(df.shape[1]-1):
        if math.isnan(df.iloc[m,n]):
            df_called.iloc[m,n] = 1000
        else:
            df_called.iloc[m,n] = input.index(int(df.iloc[m,n]))

df_called.iloc[:,:-1].max(axis=1).min() # 25

df_called.groupby(['Group']).max().min(axis=0)
#A    38
#B    30
#C    49
#D    32
#E    38

df_called[df_called.iloc[:,:-1].max(axis=1)==25]

a = df[df.Group==74]
b = df_called[df.Group==74]

s = 0
for i in range(5):
    for j in range(5):
        if b.iloc[i,j]>25:
            s+=a.iloc[i,j]
print(s*input[25]) # 32844

#############################################################################################
# Problem 2
#############################################################################################

for m in range(df.shape[0]):
    for n in range(df.shape[1]-1):
        if math.isnan(df.iloc[m,n]):
            df_called.iloc[m,n] = 0
        else:
            df_called.iloc[m,n] = input.index(int(df.iloc[m,n]))
            
# row wise
a = pd.DataFrame(df_called.iloc[:,:-1].max(axis=1))
a['Group'] = sum([[i]*5 + [0] for i in range(1,101)], [])[:-1]
a.groupby(['Group']).min().max() # 89

# col wise
df_called.groupby(['Group']).max().min(axis=1).max() # 90

# --> as for index 89 rows are already complete, 89 has to be the one and not 90. Which Group is that?
df_called.iloc[:,:-1]
a.groupby(['Group']).min()[60:80] # Group 66

a = df[df.Group==66]
b = df_called[df.Group==66]
s = 0
for i in range(5):
    for j in range(5):
        if b.iloc[i,j]>89:
            s+=a.iloc[i,j]
print(s*input[89]) # 4920
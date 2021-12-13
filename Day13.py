# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:13:06 2021

@author: Tobi
"""
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day13_Input.csv", delimiter=',', header=None)
inst = df.iloc[-12:,0]
inst = inst.str.split(" ", expand=True)
inst = inst.iloc[:,2].str.split("=", expand=True)

df = df.iloc[:-12,:].astype(int)

#############################################################################################
# Problem 1
#############################################################################################

A = pd.DataFrame(0, index=range(df.max(axis=0)[1]+2), columns=range(df.max(axis=0)[0]+1))

for i in range(df.shape[0]):
    A.iloc[df.iloc[i,1],df.iloc[i,0]] = 1

def fold(df, n, axis='x'):
    if axis=='x':
        df_new = pd.DataFrame(0, index=range(df.shape[0]), columns=range(n))
        df_new = pd.DataFrame(np.matrix(df.iloc[:,:n]) + np.matrix(df.iloc[:,-1:n:-1]))
    if axis=='y':
        df_new = pd.DataFrame(0, index=range(n), columns=range(df.shape[1]))
        df_new = pd.DataFrame(np.matrix(df.iloc[:n,:]) + np.matrix(df.iloc[-1:n:-1,:]))
    return(df_new)

for i in range(inst.shape[0]):
    if i==1:
        print(np.minimum(1,A).sum(axis=0).sum()) # <-- solution for Problem 1: 785
    A = fold(A, int(inst.iloc[i,1]), axis=inst.iloc[i,0]) 

#############################################################################################
# Problem 2
#############################################################################################

A = np.minimum(A, 1)
A = A.replace(0," ")

for i in range(0,8):
    print(A.iloc[:,i*5:5*(i+1)])
    
# FJAHJGAH
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:29:24 2021

@author: Tobi
"""

import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day11_Input.csv", dtype=str, delimiter=';', header=None)

df = df[0].str.split("", n = len(df[0][0]), expand = True)
df = df.iloc[:,1:]
df.columns = range(0,len(df.columns))
df = df.astype(int)

#############################################################################################
# Problem 1
#############################################################################################

flashes = 0
def step(df, flashes):
    df_new = df.copy()
    df_new = df_new + 1
    while any((df_new>9).any()): # <- can check with that
        for i in range(df_new.shape[0]):
            u = max(i-1, 0) # upper end of adjacent cells
            b = min(i+2, df_new.shape[0]) # bottom end of adjacent cells
            for j in range(df_new.shape[1]):
                l = max(j-1, 0) # left end of adjacent cells
                r = min(j+2, df_new.shape[1]) # right end of adjacent cells
                if df_new.iloc[i,j]>9:
                    flashes += 1
                    df_new.iloc[u:b, l:r] += 1
                    df_new.iloc[i,j] = -1000
    df_new[df_new<0] = 0
    return(df_new, flashes)

print(0, " step: ", df)
for i in range(100):
    df, flashes = step(df, flashes)
print(flashes) # 1729



#############################################################################################
# Problem 2
#############################################################################################


df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day11_Input.csv", dtype=str, delimiter=';', header=None)

df = df[0].str.split("", n = len(df[0][0]), expand = True)
df = df.iloc[:,1:]
df.columns = range(0,len(df.columns))
df = df.astype(int)

cnt = 0
while df.sum(axis=0).sum(axis=0) > 0:
    df, flashes = step(df, flashes)
    cnt += 1
print(cnt) # 237
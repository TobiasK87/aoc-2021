# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:58:22 2021

@author: Tobi
"""

df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day9_Input.csv", dtype=str, delimiter=';', index_col=None)

#############################################################################################
# Problem 1
#############################################################################################

len(df.iloc[0,0])[2]

ls = []
# 1. top row
# 1.1 left element
m = int(df.iloc[0,0][0])
if int(df.iloc[0,0][1]) > m and int(df.iloc[1,0][0]) > m:
    ls.append(m+1)
# 1.2 middle row
for j in range(1,99):
    m = int(df.iloc[0,0][j])
    if int(df.iloc[0,0][j-1]) > m and int(df.iloc[1,0][j]) > m and int(df.iloc[0,0][j+1]) > m:
        ls.append(m+1)
# 1.3 right element
m = int(df.iloc[0,0][99])
if int(df.iloc[0,0][99-1]) > m and int(df.iloc[1,0][99]) > m:
    ls.append(m+1)
# 2. middle rows
for i in range(1,df.shape[0]-1):
    m = int(df.iloc[i,0][0])
    # 2.1 left col
    if int(df.iloc[i-1,0][0]) > m and int(df.iloc[i,0][1]) > m and int(df.iloc[i+1,0][0]) > m:
        ls.append(m+1)
    # 2.2 middle cols
    for j in range(1,len(df.iloc[0,0])-1):
        m = int(df.iloc[i,0][j])
        if int(df.iloc[i-1,0][j]) > m and int(df.iloc[i,0][j-1]) > m and int(df.iloc[i,0][j+1]) > m and int(df.iloc[i+1,0][j]) > m:
            ls.append(m+1)
    # 2.3 right col
    m = int(df.iloc[i,0][99])
    if int(df.iloc[i-1,0][99]) > m and int(df.iloc[i,0][98]) > m and int(df.iloc[i+1,0][99]) > m:
        ls.append(m+1)
# 3. bottom rows
# 3.1 left element
m = int(df.iloc[99,0][0])
if int(df.iloc[99,0][1]) > m and int(df.iloc[98,0][0]) > m:
    ls.append(m+1)
# 3.2 middle row
for j in range(1,99):
    m = int(df.iloc[99,0][j])
    if int(df.iloc[99,0][j-1]) > m and int(df.iloc[98,0][j]) > m and int(df.iloc[99,0][j+1]) > m:
        ls.append(m+1)
# 3.3 right element
m = int(df.iloc[99,0][99])
if int(df.iloc[99,0][99-1]) > m and int(df.iloc[98,0][99]) > m:
    ls.append(m+1)
sum(ls)

ls


#############################################################################################
# Problem 2
#############################################################################################


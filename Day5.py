# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:38:34 2021

@author: Tobi
"""

import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day5_Input.csv", dtype=str, index_col=None)

df['A0'] = df.index
df['A0'] = df.A0.apply(str).str.strip("()").str.replace('\'','')

df[['A1', 'A2']] = df.A0.str.split(', ', expand=True)
df[['A2', 'A3']] = df.A2.str.split(' -> ', expand=True)
df = pd.DataFrame({'A1': df.A1, 'A2':df.A2, 'A3':df.A3, 'A4':df.A})

df.A1 = df.A1.apply(int)
df.A2 = df.A2.apply(int)
df.A3 = df.A3.apply(int)
df.A4 = df.A4.apply(int)
df = df[(df.A1==df.A3) | (df.A2==df.A4)]

#############################################################################################
# Problem 1
#############################################################################################

# test
df = pd.DataFrame({'A1':[0,8,9,2,7,6,0,3,0,5],'A2':[9,0,4,2,0,4,9,4,0,5],'A3':[5,0,3,2,7,2,2,1,8,8],'A4':[9,8,4,1,4,0,9,4,8,2]})
#

A = pd.DataFrame(0, index=range(1000), columns=range(1000))

for i in range(df.shape[0]):
    if df.A1[i]==df.A3[i]:
        if df.A2[i]>=df.A4[i]:
            a = df.A4[i]
            b = df.A2[i]
        else:
            a = df.A2[i]
            b = df.A4[i]
        A.iloc[a:b+1,df.A1[i]] = [a+1 for a in A.iloc[a:b+1,df.A1[i]]]
    if df.A2[i]==df.A4[i]:
        if df.A1[i]>=df.A3[i]:
            a = df.A3[i]
            b = df.A1[i]
        else:
            a = df.A1[i]
            b = df.A3[i]
        A.iloc[df.A2[i],a:b+1] = [a+1 for a in A.iloc[df.A2[i],a:b+1]]
        

len([a for a in sum(A.values.tolist(), []) if a>=2]) # 4421


#############################################################################################
# Problem 2
#############################################################################################
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day5_Input.csv", dtype=str, index_col=None)
df['A0'] = df.index
df['A0'] = df.A0.apply(str).str.strip("()").str.replace('\'','')

df[['A1', 'A2']] = df.A0.str.split(', ', expand=True)
df[['A2', 'A3']] = df.A2.str.split(' -> ', expand=True)
df = pd.DataFrame({'A1': df.A1, 'A2':df.A2, 'A3':df.A3, 'A4':df.A})

df.A1 = df.A1.apply(int)
df.A2 = df.A2.apply(int)
df.A3 = df.A3.apply(int)
df.A4 = df.A4.apply(int)
#df = df[(df.A1==df.A3) | (df.A2==df.A4)]
df = pd.DataFrame({'A1':[0,8,9,2,7,6,0,3,0,5],'A2':[9,0,4,2,0,4,9,4,0,5],'A3':[5,0,3,2,7,2,2,1,8,8],'A4':[9,8,4,1,4,0,9,4,8,2]})
df = df[(df.A1==df.A3) | (df.A2==df.A4) | (abs(df.A1-df.A3)==abs(df.A2-df.A4))]
#df = df.iloc[:2,:]

A = pd.DataFrame(0, index=range(1000), columns=range(1000))
cnt=0
for i in range(df.shape[0]):
    if df.A1[i]==df.A3[i]:
        if df.A2[i]>=df.A4[i]:
            a = df.A4[i]
            b = df.A2[i]
        else:
            a = df.A2[i]
            b = df.A4[i]
        A.iloc[a:b+1,df.A1[i]] = [a+1 for a in A.iloc[a:b+1,df.A1[i]]]
        cnt+=1
    if df.A2[i]==df.A4[i]:
        if df.A1[i]>=df.A3[i]:
            a = df.A3[i]
            b = df.A1[i]
        else:
            a = df.A1[i]
            b = df.A3[i]
        A.iloc[df.A2[i],a:b+1] = [a+1 for a in A.iloc[df.A2[i],a:b+1]]
        cnt+=1
    if abs(df.A1[i]-df.A3[i])==abs(df.A2[i]-df.A4[i]):
        if (df.A1[i]<=df.A3[i]) and (df.A2[i]<=df.A4[i]):
            for m in range(df.A1[i],df.A3[i]+1):
                A.iloc[m,m] += 1
            cnt+=1
        if (df.A1[i]<=df.A3[i]) and (df.A2[i]>=df.A4[i]):
            for idx,m in enumerate(range(df.A1[i],df.A3[i]+1)):
                A.iloc[df.A2[i]-idx,m] += 1
            cnt+=1
        if (df.A1[i]>=df.A3[i]) and (df.A2[i]<=df.A4[i]):
            for idx,m in enumerate(range(df.A2[i],df.A4[i]+1)):
                A.iloc[m, df.A1[i]-idx] += 1
            cnt+=1
        if (df.A1[i]>=df.A3[i]) and (df.A2[i]>=df.A4[i]):
            for idx,m in enumerate(range(df.A1[i],df.A3[i]-1,-1)):
                A.iloc[df.A2[i]-idx,m] += 1
            cnt+=1
cnt
        
A.iloc[:10,:10]
        
len([a for a in sum(A.values.tolist(), []) if a>=2]) # 14875 is too low, # 15000 is too low

len([a for a in sum(A.values.tolist(), []) if a==2]) # 12280
len([a for a in sum(A.values.tolist(), []) if a==3]) # 727
len([a for a in sum(A.values.tolist(), []) if a==4]) # 831
len([a for a in sum(A.values.tolist(), []) if a==5]) # 130
len([a for a in sum(A.values.tolist(), []) if a==6]) # 31
len([a for a in sum(A.values.tolist(), []) if a==7]) # 25
len([a for a in sum(A.values.tolist(), []) if a==8]) # 4
len([a for a in sum(A.values.tolist(), []) if a==9]) # 20
len([a for a in sum(A.values.tolist(), []) if a==10]) # 36
pd.Series([a for a in sum(A.values.tolist(), []) if a>=2]).value_counts()



#############################################################################################
# Playing


B = pd.DataFrame({0:[2,3],1:[5345,123]})
C = B.values.tolist()
sum(C,[])

[1,2,3]+1



df.loc[:,['A0','A']]

df[['A1','A2']] = df.A0.apply(str).str.split("->", expand=True)
df[['A3','A4']] = df.A1.str.split(",", expand=True)
df['A3'] = df.A3.str.strip('\'(')
df['A4'] = df.A4.str.replace('\'','')



str.split("->", expand=True)


df = df.iloc[:,-1:]

df[['old','new']] = 
df.A.str.split("->", expand=True)[0]

df.iloc[0,0]
df.index[0]

type(df.A[0])
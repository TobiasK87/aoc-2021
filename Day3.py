# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:21:24 2021

@author: Tobi
"""

import pandas as pd
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day3_Input.csv", dtype=str, sep=',')

#############################################################################################
# Problem 1
#############################################################################################

df = df["123456789XYZ"].str.split("", n = len(df["123456789XYZ"][0]), expand = True)
df.apply(int)
df.describe()
df[6].describe()
# --> x = 101000101001
A = '101000101001'
B = ["".join([str(int(1-int(a))) for a in A])]
A = [A]
x = sum([int(x)*2**(len(A[0])-1-i) for i, x in enumerate(A[0])])
y = sum([int(x)*2**(len(B[0])-1-i) for i, x in enumerate(B[0])])
print(x * y) # 3885894

#############################################################################################
# Problem 2
#############################################################################################

# oxygen generator rating
df2 = df.copy()
i = 1
while df2.shape[0]>1:
    if len(df2[i].mode())>1:
        df2 = df2[df2[i]=='1']
    else:
        df2 = df2[df2[i]==df2[i].mode()[0]]
    i+=1
print(df2)
bin_to_dec('111010111111') # 3775
        
# CO2 scrubber rating
df2 = df.copy()
i = 1
while df2.shape[0]>1:
    if len(df2[i].mode())>1:
        df2 = df2[df2[i]=='0']
    else:
        df2 = df2[df2[i]==df2[i].value_counts().idxmin()[0]]
    i+=1
print(df2)
bin_to_dec('010010000111') # 1159
print(3775*1159) # 4375225


#############################################################################################
# function
#############################################################################################

def bin_to_dec(string):
    A = [string]
    return sum([int(x)*2**(len(A[0])-1-i) for i, x in enumerate(A[0])])

bin_to_dec('101000101001')
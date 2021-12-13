# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:39:06 2021

@author: Tobi
"""

import pandas as pd
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day2_Input.csv", sep=' ')

#############################################################################################
# Problem 1
#############################################################################################

x = sum(df.loc[df.direction=='forward', 'num'])
y = sum(df.loc[df.direction=='down', 'num']) - sum(df.loc[df.direction=='up', 'num'])
print(x*y) # 1727835

#############################################################################################
# Problem 2
#############################################################################################

df.loc[df.direction=='up','num'] = -df.loc[df.direction=='up','num']

df.loc[df.direction=='forward','aim'] = 0
df.loc[df.direction!='forward','aim'] = df.loc[df.direction!='forward','num']

df['aim_cum'] = df['aim'].cumsum()

df.loc[df.direction=='forward','x'] = df.loc[df.direction=='forward','num']

df.loc[df.direction!='forward','x'] = 0
df['x'] = df['x'].cumsum()

df['y'] = 0
df.loc[df.direction=='forward','y'] = df.loc[df.direction=='forward','num'] * df.loc[df.direction=='forward','aim_cum']
df['y'] = df['y'].cumsum()
print(df.iloc[-1,-2]*df.iloc[-1,-1]) # 1544000595

#############################################################################################
# Exploring
#############################################################################################

df['x'] = df.groupby('direction')['num'].cumsum()

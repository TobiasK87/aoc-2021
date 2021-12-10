# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:53:14 2021

@author: Tobi
"""

import pandas as pd
from itertools import cycle

df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day1_Input.csv")

#############################################################################################
# Problem 1
#############################################################################################

df['lagged'] = df.shift(periods=1)
df.loc[df.loc[:,"ColName"]>df.loc[:,"lagged"],].shape[0] # 1752

#############################################################################################
# Problem 2
#############################################################################################

# THIS HERE IS NOT EVEN NECESSARY
As = cycle(['A']*3 + [''])
Bs = cycle(['B']*3 + [''])
Cs = cycle(['C']*3 + [''])
Ds = cycle(['D']*3 + [''])
df['As'] = [next(As) for A in range(len(df))]
df['Bs'] = [''] + [next(Bs) for B in range(len(df)-1)]
df['Cs'] = ['']*2 + [next(Cs) for C in range(len(df)-2)]
df['Ds'] = ['']*3 + [next(Ds) for D in range(len(df)-3)]
# END OF NOT NECESSARY

df['sumed'] = df["ColName"].shift(periods=-1) + df["ColName"].shift(periods=0) + df["ColName"].shift(periods=1)
df['sumed_lagged'] = df['sumed'].shift(periods=1)

df.loc[df.loc[:,"sumed"]>df.loc[:,"sumed_lagged"],].shape[0] # 1781 <-- result


# Playing

df.head()

df.index = pd.date_range('2021-01-01', periods=df.shape[0], freq='2D')
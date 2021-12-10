# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:46:42 2021

@author: Tobi
"""

import pandas as pd
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\AdventOfCode\2021\Day8_Input.csv", dtype=str, delimiter=';', index_col=None)

#############################################################################################
# Problem 1
#############################################################################################

poss = [2,3,4,7]
out1 = len([a for a in df.Output1 if len(a) in poss])
out2 = len([a for a in df.Output2 if len(a) in poss])
out3 = len([a for a in df.Output3 if len(a) in poss])
out4 = len([a for a in df.Output4 if len(a) in poss])
print(out1+out2+out3+out4) # 288


#############################################################################################
# Problem 2
#############################################################################################

def trans(x):
    return list(x)

df = df.apply(trans) # does not work properly for some reason

a = df.iloc[0,:]

df.Input1[:10]
df.Input1.apply(trans)[:10]

df.apply(trans).iloc[0,:]

a[0]
type(a)
def identify(srs):
    dic = {}
    for s in srs:
        if len(s)==2:
            dic[1] = s
        if len(s)==3:
            dic[7] = s
        if len(s)==4:
            dic[4] = s
        if len(s)==7:
            dic[8] = s
        if len(s)==5:
            for r in [a for a in srs if len(a)==5 and len(list(set(a+s)))>5]:
                #print("r:")
                if len(set(s+r))==6:
                    for t in [a for a in srs if len(a)==5 and len(list(set(a+r)))>5 and len(list(set(a+s)))>5]:
                        print("r:",r,"s:",s,"t:",t)
                        if len(set(s+r))==6 and len(set(s+t))==6:
                            dic[3] = s
                            #print(1,r,s,t)
                        if len(set(r+s))==6 and len(set(r+t))==6:
                            dic[3] = s
                            #print(2,r,s,t)
                        if len(set(t+r))==6 and len(set(t+s))==6:
                            dic[3] = s
                            #print(3,r,s,t)
    return(dic)

identify(df.iloc[0,:11])
df.iloc[0,:11]

set([5,3,2]) - set([2,5])

set([1,2,3,4,5]).intersection(set([2,3,4,5]),set([2,3,6]))

a = df.iloc[0,:11]
list(a)[0]
[b for b in list(a)]
a.apply(list)[0]
[e for e in [b for b in a][0]]

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

df = df.apply(trans) # does not work properly for some if trans returns (sorted(list(x)) for some reason

def identify(srs):
    dic = {}
    while len(dic.values())<10:
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
                            #print("r:",r,"s:",s,"t:",t)
                            if len(set(s+r))==6 and len(set(s+t))==6:
                                dic[3] = s
                                #print(1,r,s,t)
                            if len(set(r+s))==6 and len(set(r+t))==6:
                                dic[3] = r
                                #print(2,r,s,t)
                            if len(set(t+r))==6 and len(set(t+s))==6:
                                dic[3] = t
                                #print(3,r,s,t)
                if dic.get(9,0)!=0 and dic.get(3,0)!=0:
                    temp = list(set(dic[9]) - set(dic[3]))[0]
                    if temp in s:
                        dic[5] = s
                        for r in [a for a in srs if len(a)==5 and a!=dic[3] and a!=dic[5]]:
                            dic[2] = r
                    elif s!=dic[3]:
                        dic[2] = s
                        for r in [a for a in srs if len(a)==5 and a!=dic[3] and a!=dic[2]]:
                            dic[5] = r
            if len(s)==6:
                # find encoding of 0
                for idx, s5 in enumerate([a for a in srs if len(a)==5]):
                    if idx==0:
                        S5 = set(s5)
                    S5 = S5.intersection(set(s5))
                S5 = list(S5)
                # print("s in len(s)==6: ", s)
                # print("S5", S5)
                for a in S5:
                    if a not in s:
                        #print("in if", dic)
                        horizontal_middle = a
                        dic[0] = s
                if dic.get(0,0)!=0 and dic.get(1,0)!=0:
                    temp = set()
                    temp = set(dic[0]) - set(dic[1])
                    temp.add(horizontal_middle)
                    if len(temp.intersection(set(s))) == 5:
                        dic[6] = s
                    if dic.get(6,0)!=0:
                        if dic[6]!=s and dic[0]!=s:
                            dic[9] = s
    return(dic)

df['decoded'] = 0
for i in range(df.shape[0]):
    d = identify(df.iloc[i,:10])
    inv_map = {v: k for k, v in d.items()}
    d2 = {}
    for m in inv_map.keys():
        # print(sorted(i))
        a = sorted(m)
        d2[''.join(sorted(m))] = inv_map[m]
    
    out = ""
    for k in range(4):
        out += str(d2["".join(sorted(df.iloc[i,10:14][k]))])
    df.iloc[i,14] = int(out)

print(sum(df.decoded)) # 940724



# more elegant but does not work, yet
df["dic"] = df.apply(lambda x: identify(df.iloc[x,0:10]), axis=0)
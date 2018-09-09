#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:57:22 2018

@author: xutingxi
"""
'''
迪杰斯特拉算法
'''
import copy
routelist=[[0,1,5,1000,1000,1000,1000,1000,1000],
           [1,0,3,7,5,1000,1000,1000,1000],
           [5,3,0,1000,1,7,1000,1000,1000],
           [1000,7,1000,0,2,1000,3,1000,1000],
           [1000,5,1,2,0,3,6,9,1000],
           [1000,1000,7,1000,3,0,1000,5,1000],
           [1000,1000,1000,3,6,1000,0,2,7],
           [1000,1000,1000,1000,9,5,2,0,4],
           [1000,1000,1000,1000,1000,1000,7,4,0]]
startID=0
def Dshortpath(routhlist,startID):
    n=len(routelist)
    D=routelist[startID]
    final=[i*0 for i in range(n)]
    p=copy.deepcopy(final)
    final[startID]=1
    for i in range(1,n):
        minvalue=1000
        for w in range(n):            
            if not final[w] and D[w]<minvalue:
                k=w
                minvalue=D[w]
        final[k]=1
        #修正最小值
        for w in range(n):
            if not final[w] and minvalue+routelist[k][w]<D[w]:
                D[w]=minvalue+routelist[k][w]
                p[w]=k        
    return  p








a={(1,2):9}
b=a.copy()
b[(1,2)]=2




a='a'
print (a > 'b' and 'c')




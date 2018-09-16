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




routelist=[[0,1,5,1000,1000,1000,1000,1000,1000],
           [1,0,3,7,5,1000,1000,1000,1000],
           [5,3,0,1000,1,7,1000,1000,1000],
           [1000,7,1000,0,2,1000,3,1000,1000],
           [1000,5,1,2,0,3,6,9,1000],
           [1000,1000,7,1000,3,0,1000,5,1000],
           [1000,1000,1000,3,6,1000,0,2,7],
           [1000,1000,1000,1000,9,5,2,0,4],
           [1000,1000,1000,1000,1000,1000,7,4,0]]
import numpy as np
def ShortestPath_Dijkstra(route):
    citys = len(route)
    visited = [i*0 for i in range(citys)]
    visited[0] = 1
    parent = [i*0 for i in range(citys)]
    for w in range(citys):
        minRoute = 1000
        for i in range(1,citys):
            if not visited[i] and route[0][i] < minRoute:
                minRoute = route[0][i]
                k = i
        visited[k] = 1
        for j in range(1,citys):
            if not visited[j] and route[0][j] > route[0][k]+route[k][j]:
                route[0][j] = route[0][k]+route[k][j]
                parent[j] = k
    result = []

    return parent
ShortestPath_Dijkstra(routelist)





#定义Floyd

routelist=[[0,1,5,1000,1000,1000,1000,1000,1000],
           [1,0,3,7,5,1000,1000,1000,1000],
           [5,3,0,1000,1,7,1000,1000,1000],
           [1000,7,1000,0,2,1000,3,1000,1000],
           [1000,5,1,2,0,3,6,9,1000],
           [1000,1000,7,1000,3,0,1000,5,1000],
           [1000,1000,1000,3,6,1000,0,2,7],
           [1000,1000,1000,1000,9,5,2,0,4],
           [1000,1000,1000,1000,1000,1000,7,4,0]]
def ShortestPath_Floyd(route):
    citys = len(route)
    P = []
    for i in range(citys):
        p = []
        for j in range(citys):
            p.append(j)
        P.append(p)
    for k in range(citys):
        for v in range(citys):
            for w in range(citys):
                if route[v][w]>route[v][k] + route[k][w]:
                    route[v][w] = route[v][k] + route[k][w]
                    P[v][w] = P[v][k]
    return P

ShortestPath_Floyd(routelist)
'''
图的定义
图的数据结构----邻接矩阵和邻接链表
图的遍历
最小生成树
最短路径
拓扑排序
关键路径
'''

import numpy as np
# 图的遍历    深度优先，递归，邻接矩阵

G = [[0,1,0,0,0,1,0,0,0],
     [1,0,1,0,0,0,1,0,1],
     [0,1,0,1,0,0,0,0,1],
     [0,0,1,0,1,0,1,1,1],
     [0,0,0,1,0,1,0,1,0],
     [1,0,0,0,1,0,1,0,0],
     [0,1,0,1,0,1,0,1,0],
     [0,0,0,1,1,0,1,0,0],
     [0,1,1,1,0,0,0,0,0]
     ]

class DeepSearch(object):
    def __init__(self,G):
        self.n = len(G)
        self.G = G
        self.visited = np.zeros([1, self.n], int)[0]
        self.route = []
    def DFS(self,s):
        self.visited[s] = 1
        self.route.append(s)
        for j in range(self.n):
            if not self.visited[j] and self.G[s][j] == 1:
                self.DFS(j)
        return
    def DFSSearch(self):
        for i in range(self.n):
            if not self.visited[i]:
                 self.DFS(i)
        return self.route

mysearch = DeepSearch(G)
myroute = mysearch.DFSSearch()
print(myroute)



#广度优先   就是将元素存入队列中




#构造最小生成树  Prim算法

G = [[0,10,3,5],
     [10,0,1000,7],
     [3,1000,0,20],
     [5,7,20,0]]

class MinGenTree(object):
    def __init__(self,G):
        self.route = []
        self.ver = [0]
        self.length = len(G)
        self.G = G
        self.minL = 65535
    def mingentree(self):
        minL = 65535
        for i in range(1,self.length):
            if self.G[0][i] != 0 and self.G[0][i] < minL:
                minL = self.G[0][i]
                k = i
        self.route.append([0,k])
        self.ver.append(k)
        while len(self.ver) < self.length:
            minL = 65535
            for k in self.ver:
                for i in range(self.length):
                    if i not in self.ver and self.G[k][i] < minL:
                        minL = self.G[k][i]
                        s = i
                        finalk = k
            self.route.append([finalk,s])
            self.ver.append(s)
        return self.route

mymingentree = MinGenTree(G)
myroute = mymingentree.mingentree()
print(myroute)

#构造最小生成树  Kruskal算法




#最短路径 Dijkstra 算法
G = [[0,1,5,1000,1000],
     [1,0,3,7,5],
     [5,3,0,1000,1],
     [1000,7,1000,0,2],
     [1000,5,1,2,0]]

class ShortRoute(object):
    def __init__(self):
        pass
    def Dijkstra(self,start,end,G):

        n = len(G)
        P = np.zeros([1,n],int)[0]
        for i in range(n):
            P[i] = start
        state = np.zeros([1,n],int)[0]
        state[start] = 1
        for count in range(n):
            minL = 65535
            for i in range(n):
                if G[start][i] < minL and not state[i]:
                    minL = G[start][i]
                    k = i
            state[k] = 1
            for j in range(n):
                if not state[j] and minL+G[k][j] < G[start][j]:
                    G[start][j] = minL+G[k][j]
                    P[j] = k
        myroute =[end]
        index = end
        while index != start:
            myroute.insert(0,P[index])
            index = P[index]
        return myroute

myshortroute = ShortRoute()
myroute = myshortroute.Dijkstra(2,3,G)
print(myroute)




#判断有向图的连通性

def DFSSearch(n, G, start):
    route = [start]
    visited = []
    for i in range(n):
        visited.append(0)

    def DFS(s):
        visited[s] = 1
        route.append(s)
        for j in range(n):
            if not visited[j]:
                DFS(j)
        return

    visited[start] = 1
    begin = start
    for i in range(n):
        if not visited[i] and G[begin][i] != 65500:
            DFS(i)
    return route
start =0
n=3
if len(DFSSearch(n, G, start)) != n:
    print("不是连通图")





























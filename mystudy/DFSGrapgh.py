class DFSGraph(object):
    '''
    这仅是深度优先遍历，并不是求解最短路径。
    '''
    def __init__(self,Graph):
        self.Graph = Graph
        self.VexsNum = len(Graph[0])
        self.visited = [0 for i in range(self.VexsNum)]
        self.Routes = []


    def DFS(self,i):
        self.visited[i] = 1
        route = [i]
        for j in range(self.VexsNum):
            if self.Graph[i][j] and not self.visited[j]:
                print(i,j)
                route.extend(self.DFS(j))
        return route

    def DFSTraverse(self):
        for i in range(self.VexsNum):
            if not self.visited[i]:
                self.Routes.append(self.DFS(i))
        return self.Routes

Graph = [[0,1,1,0,1],
         [1,0,1,1,0],
         [1,1,0,1,1],
         [0,1,1,0,0],
         [1,0,1,0,0]]

myDFSGraph = DFSGraph(Graph)
Routes = myDFSGraph.DFSTraverse()



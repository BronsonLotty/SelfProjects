

adj_matrix = [[0,9,8,65500],
             [65500,0,11,30],
              [65500,65500,0,20],
              [65500,65500,65500,0]]


def broadcast_delivery_time(origin_id, adj_matrix):
    # Enter your code here.
    def Dijkstra(start, end, G, num_lines):

        n = num_lines
        P = []
        state = []
        for i in range(n):
            P.append(0)
        for i in range(n):
            P[i] = start
        for i in range(n):
            state.append(0)
        state[start] = 1
        for count in range(n):
            minL = 655350000
            for i in range(n):
                if G[start][i] < minL and not state[i]:
                    minL = G[start][i]
                    k = i
            state[k] = 1
            for j in range(n):
                if not state[j] and  minL + G[k][j] < G[start][j]:
                    G[start][j] = minL + G[k][j]
                    P[j] = k
        myroute = [end]
        index = end
        while index != start:
            myroute.insert(0, P[index])
            index = P[index]
        length = 0
        for i in range(len(myroute) - 1):
            length += G[myroute[i]][myroute[i + 1]]
        return length

    def DFSSearch(n, G,start):
        route = [start]
        visited = []
        for i in range(n):
            visited.append(0)
        def DFS(s):
            visited[s] = 1
            route.append(s)
            for j in range(n):
                if not visited[j] and G[s][j] != 65500:
                    DFS(j)
            return
        visited[start] = 1
        begin = start
        for i in range(n):
            if not visited[i] and G[begin][i] != 65500:
                DFS(i)
        return route

    counts_route = len(DFSSearch(num_lines, adj_matrix,origin_id))
    if counts_route != num_lines :
        return None
    else:
        maxlength = 0
        for i in range(num_lines):
            newlength = Dijkstra(origin_id, i, adj_matrix, num_lines)
            if newlength > maxlength:
                maxlength = newlength

    return maxlength
num_lines = 4
print(broadcast_delivery_time(0, adj_matrix))
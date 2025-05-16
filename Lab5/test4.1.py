from collections import deque

def BFS(adj, S, parent, dist):
    q = deque()
    dist[S-1] = 0
    q.append(S)

    while len(q) != 0:
        u = q.popleft()
        for v in adj[u-1]:
            if dist[v-1] == float('inf'):
                parent[v-1] = u
                dist[v-1] = dist[u-1]+1
                q.append(v)

def get_path(adj, S, D, V):
    parent = [None]*V
    dist = [float('inf')]*V
    BFS(adj, S, parent, dist)
    if dist[D-1] == float('inf'):
        return(-1)
    
    path = []
    cur = D
    path.append(D)
    while parent[cur-1] != None:
        path.append(parent[cur-1]) 
        cur = parent[cur-1]

    return(path)

V, E, S, D, K = list(map(int, input().split()))
adj_lst = [None]*V
for a in range(V):
    adj_lst[a] = []
if E != 0:
    for i in range(E):
        st, en = list(map(int, input().split()))
        adj_lst[st-1].append(en)
    for each in adj_lst:
        each.sort()

path_SK = get_path(adj_lst, S, K, V)
if path_SK != -1:
    path_KD = get_path(adj_lst, K, D, V)
    if path_KD != -1:

        if len(path_SK) == 1:
            path = path_KD
            print(len(path_KD)-1)
        elif len(path_KD) == 1:
            print(len(path_SK)-1)
            path = path_SK
        else:
            print(len(path_KD)+len(path_SK)-1)
            path = path_SK+path_KD[1:]
        
        for i in range(1, len(path)):
            print(path[len(path)-i], end=" ")
        print(path[0])

    else:
        print(-1)
else:
    print(-1)
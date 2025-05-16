from collections import deque

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

def BFS(adj, S, D, V):
    exp = [0]*V
    parent = [-1]*V
    q = deque()
    q.append(S)
    exp[S-1] = 1

    while len(q) != 0:
        u = q.popleft()
        if u == D:
            break
        for v in adj[u-1]:
            if exp[v-1] == 0:
                exp[v-1] = 1
                parent[v-1] = u
                q.append(v)
    
    if exp[D-1] == 0:
        return -1
    else:
        path = []
        cur = D
        while cur != -1:
            path.append(cur)
            cur = parent[cur-1]
        return path[::-1]
    
SK = BFS(adj_lst, S, K, V)
KD = BFS(adj_lst, K, D, V)

if SK == -1 or KD == -1:
    print(-1)
else:
    path = SK+KD[1:]
    print(len(path)-1)
    print(*path)
from collections import deque
import sys
sys.setrecursionlimit(2*100000+5)

def get_path(adj_lst, S, D):
    
    color = [0]*V
    parent = [-1]*V
    Q = deque()

    Q.append(S)

    color[S-1] = 1
    while len(Q)  != 0:
        u = Q.popleft()
        for v in adj_lst[u-1]:
            if color[v-1] == 0:
                Q.append(v)
                color[v-1] = 1
                parent[v-1] = u

    if S == D:
        return(0, [S])

    cur = D-1
    to_print = [D]
    cnt = 0
    while parent[cur] != -1:
        if parent[cur] == S:
            to_print.append(parent[cur])
            cnt += 1
            break
        to_print.append(parent[cur])
        cnt += 1
        cur = parent[cur]-1

    if S != D:
        if cnt != 0:
        # if to_print[-1] == S:
            return (cnt, to_print)
        else:
            return (-1, -1)

V, E, S, D, K = list(map(int, input().split()))
adj_lst = [None]*V
for a in range(V):
    adj_lst[a] = []
if E != 0:
    for i in range(E):
        st, en = list(map(int, input().split()))
        adj_lst[st-1].append(en)

# for each in adj_lst:
#     each.sort()

nodes_SK, path_SK = get_path(adj_lst, S, K)
if nodes_SK != -1 :
    nodes_KD, path_KD = get_path(adj_lst, K, D)
    if nodes_KD != -1:
        print(nodes_SK+nodes_KD)
        if len(path_SK) == 1:
            path = path_KD
        elif len(path_KD) == 1:
            path = path_SK
        else:
            path = path_SK+path_KD[1:]

        for i in range(1, len(path)):
            print(path[len(path)-i], end=" ")
        print(path[0])
    else:
        print(-1)
else:
    print(-1)
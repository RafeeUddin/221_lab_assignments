from collections import deque
import sys
sys.setrecursionlimit(2*100000+5)


N = int(input())
xi, yi, xf, yf = list(map(int, input().split()))

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
parent = [None]*N**2
time = [float("inf")]*N**2
adj = {}

start = ((xi-1)*N)+(yi-1)
end = ((xf-1)*N)+(yf-1)

time[start] = 0

def knight(st, call = None):
    xc, yc = divmod(st, N)
    t = time[st]
    for x, y in moves:
        if 0<= xc+x <N and 0<= yc+y < N:
            new = (xc+x)*N + (yc+y)
            if st not in adj:
                adj[st] = {new}
            else:
                adj[st].add(new)

            if t+1 < time[new]: 
                time[new] = t+1
                parent[new] = st

    # print(st, adj[st])
    visited = {}
    for v in adj[st]:
        if st not in visited.keys():
            visited[st] = set()

        # print(v, time[v], st, time[st])
        if v == end or v == parent[st] or v in visited[st]:
        # if v == end or v == parent[st] or v == call:
            continue
        else: 
             if time[v] <= time[st]+1:
                visited[st].add(v)
                knight(v, st)

knight(start)
# print(time)
# print(parent)
# print(adj)
if time[end] != float('inf'):
    print(time[end])
else:
    print(-1)
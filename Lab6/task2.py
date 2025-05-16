import sys
sys.setrecursionlimit(2*100000+5)
from collections import deque

def make_adj (N, M):
    # print(N, M)
    adj = []
    for n in range(N):
        adj.append([])
    # print(adj)
    for m in range(M):
        s,e = list(map(int, (input().split())))

        # if e not in adj[s-1]: 
        adj[s-1].append(e)
        # if s not in adj[e-1]:
        adj[e-1].append(s)

    # print(adj)
    return adj

def chk_bi(adj, V, visited, q, clr, teams, x = 0):

    q.append(x)
    clr[x] = int(max(teams, key=teams.get))
    visited[x] = True
    teams[max(teams, key=teams.get)] += 1
    while len(q) != 0:

        i = q.popleft()
        for j in adj[i]:

            if clr[j-1] == None:

                clr[j-1] = 1 - clr[i]
                visited[j-1] = True
                q.append(j-1)

                if clr[j-1] == 0:
                    teams['0'] += 1
                else:
                    teams['1'] += 1

    # return max(teams.values())

V, E = list(map(int, (input().split())))
# print(N, M)
adj = make_adj(V, E)
visited = [False]*V
q = deque()
clr = [None]*V

res = 0
# teams = {"1": 0, "0": 0} 

for v in range(V):

    if visited[v] == False: 
        teams = {"1": 0, "0": 0}    
        (chk_bi(adj, V, visited, q, clr, teams, x = v))
        res += max(teams.values())

print(res)
from collections import deque
import sys
sys.setrecursionlimit(2*100000+5)

def get_distance(u, adj):
    n = len(adj)
    dist = [-1]*n
    dist[u] = 0

    q = deque()
    q.append(u)

    timbaktu = u

    while q:
        cur = q.popleft()
        for v in adj[cur]:
            if dist[v] == -1:
                dist[v] = dist[cur] + 1
                q.append(v)
                if dist[v] > dist[timbaktu]:
                    timbaktu = v
    
    return timbaktu, dist[timbaktu]

V = int(input())
adj = [[] for  _ in range(V + 1)]

for i in range(V - 1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

nowhere, d1 = get_distance(1, adj)
somewhere, d2 = get_distance(nowhere, adj)

print(d2)
print(nowhere, somewhere)
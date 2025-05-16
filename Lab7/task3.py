from collections import deque
import heapq

V, E = map(int, input().split())
adj = {i: [] for i in range(1, V+1)}
for e in range(E):
    s, d, w = map(int, input().split())
    adj[s].append((d, w))
    adj[d].append((s, w))
# print(adj)

danger = [float('inf')]*(V+1)
h = []
danger[1] = 0
heapq.heappush(h, (0, 1))

while h:
    du, u = heapq.heappop(h)

    if du > danger[u]:
        continue

    for v, w in adj[u]:
        du_v = max(du, w)

        if du_v < danger[v]:
            danger[v] = du_v
            heapq.heappush(h, (danger[v], v))

for j in range(len(danger)):
    if danger[j] == float('inf'):
        danger[j] = -1
print(" ".join(map(str, danger[1:])))
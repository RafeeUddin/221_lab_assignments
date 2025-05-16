import heapq

V, E, S, D = map(int, input().split())

adj = {i : [] for i in range(V+1)}
dist_1 = [float('inf')]*(V+1)
dist_2 = [float('inf')]*(V+1)

for e in range(E):
    s, d, w = map(int, input().split())
    adj[s].append((d, w))
    adj[d].append((s, w))
# print(adj)

dist_1[S] = 0
h = []
heapq.heappush(h, (0, S))

while h:
    du, u = heapq.heappop(h)

    for v, dv in adj[u]:
        new = du + dv

        if new < dist_1[v]:
            dist_2[v] = dist_1[v]
            dist_1[v] = new
            heapq.heappush(h, (new, v))

        if dist_1[v] < new < dist_2[v]:
            dist_2[v] = new
            heapq.heappush(h, (new, v))

print(dist_2[D] if dist_2[D] != float('inf') else -1)
        

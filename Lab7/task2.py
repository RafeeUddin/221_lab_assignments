import heapq

V, E, N1, N2 = map(int, input().split())

adj = {i:[] for i in range(1, V+1)}

for e in range(E):
    f, t, w = map(int, input().split())
    adj[f].append((t, w))

# print(adj)

def dijkstra(N, adj):
    dist = [float('inf')]*(V+1)
    h = []
    heapq.heappush(h, (0, N))
    dist[N] = 0

    while h:
        du, u = heapq.heappop(h)
        if du > dist[u]:
            continue
        for v, w in adj[u]:
            d_ = dist[u] + w
            if d_ < dist[v]:
                dist[v] = d_
                heapq.heappush(h, (dist[v], v))

    return dist

dist_1 = dijkstra(N1, adj)
dist_2 = dijkstra(N2, adj)

# print(dist_1)
# print(dist_2)

common = []
for i in range(V+1):
    if max(dist_1[i], dist_2[i]) != None and max(dist_1[i], dist_2[i]) != float('inf'):
        common.append((max(dist_1[i], dist_2[i]), i))
        # print((max(dist_1[i], dist_2[i]), i))
# print(common)

if common:
    m_d, m_i = min(common)
    print(m_d, m_i)
else:
    print(-1)

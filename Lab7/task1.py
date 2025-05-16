import heapq

N, E, S, D = map(int, input().split())
F = list(map(int, input().split()))
T = list(map(int, input().split()))
W = list(map(int, input().split()))

adj = {i: [] for i in range(1, N+1)}
for i in range(E):
    adj[F[i]].append((T[i], W[i]))

# print(adj)

parent = [None]*(N+1)
dist = [float("inf")]*(N+1)
h = []

dist[S] = 0
heapq.heappush(h, (dist[S], S))

while h:
    du, u = heapq.heappop(h)
    # print(u)
    
    if du > dist[u]:
        continue

    for v, w in adj[u]:

            d_ = dist[u] + w
            if d_ < dist[v]:
                dist[v] = d_
                parent[v] = u
                heapq.heappush(h, (dist[v], v))

if dist[D] == float("inf"):
    print(-1)
else:
    path = [D]
    cur = parent[D]
    while cur != None:
        path.append(cur)
        cur = parent[cur]

    print(dist[D])
    print(" ".join(map(str, reversed(path))))


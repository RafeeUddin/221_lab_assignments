import heapq

V, E = map(int, input().split())

S = list(map(int, input().split()))
D = list(map(int, input().split()))
W = list(map(int, input().split()))

adj = {i: [] for i in range(1, V+1)}
for e in range(E):
    adj[S[e]].append((D[e], W[e]))
# print(adj)

h = []
path = [[float('inf')] * 2 for _ in range(V+1)]
path[1][0] = 0
path[1][1] = 0
heapq.heappush(h, (0, 1, -1))
# print(path)

while h:
    du, u, p = heapq.heappop(h)
    # if du > path[u][w%2]:
    #     continue
    for v, w in adj[u]:
        if p != -1 and p == (w%2):
            continue
        path_n = du + w
        # print(v)
        if path_n < path[v][w%2]:
            path[v][w%2] = path_n
            heapq.heappush(h, (path_n, v, w%2))

# print(path)
path_cost = min(path[V][0], path[V][1])
print(path_cost if path_cost != float('inf') else -1)
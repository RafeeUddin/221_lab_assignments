import heapq

V, E, S, D = map(int, input().split())
n_cost = [0]
n_cost.extend(list(map(int, input().split())))
# print(n_cost)

adj = {i: [] for i in range(1, V+1)}

for e in range(E):
    s, d = map(int, input().split())
    adj[s].append(d)
    # adj[d].append(s)
# print(adj)

p_cost = [float('inf')]*(V+1)
h = []
p_cost[S] = n_cost[S]
heapq.heappush(h, (p_cost[S], S))

while h:
    p, u = heapq.heappop(h)
    if p > p_cost[u]:
        continue
    for v in adj[u]:
        new_cost = p + n_cost[v]
        if new_cost < p_cost[v]:
            p_cost[v] = new_cost
            heapq.heappush(h, (p_cost[v], v))
    
if p_cost[D] == float('inf'):
    print(-1)
else:
    print(p_cost[D])
import heapq

def get_rep(u):
    if rep[u] != u:
        rep[u] = get_rep(rep[u])
    return rep[u]

V, E = map(int, input().split())
# adj = {i: [] for i in range(1, V+1)}
rep = [i for i in range(V+1)]
size = [1 for j in range(V+1)]
h = []
cost = 0

for e in range(E):
    S, D, W = map(int, input().split())
    # adj[s].append((d, w))
    # adj[d].append((s, w))
    heapq.heappush(h, (W, S, D))
# print(rep)

while h:
    w, s, d = heapq.heappop(h)
    rep_u, rep_v = get_rep(s), get_rep(d)

    if rep_u != rep_v:
        if size[rep_u] < size[rep_v]:
            rep_u, rep_v = rep_v, rep_u
        size[rep_u] += size[rep_v]
        rep[rep_v] = rep_u
        cost += w
    
print(cost)


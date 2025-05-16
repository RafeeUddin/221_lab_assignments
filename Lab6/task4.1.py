import sys
sys.setrecursionlimit(2*100000+5)

def make_adj(V):
    adj = []
    for _ in range(V):
        adj.append([])

    for _ in range(V-1):
        s, e = map(int, input().split())
        adj[s-1].append(e-1)
        adj[e-1].append(s-1)

    return adj

def get_subtree(u, p, adj, subsize):
    subsize[u] = 1  # count self
    for v in adj[u]:
        if v == p:
            continue
        get_subtree(v, u, adj, subsize)
        subsize[u] += subsize[v]

V, R = map(int, sys.stdin.readline().split())
adj = make_adj(V)

subsize = [0] * V
get_subtree(R - 1, -1, adj, subsize)

Q = int(sys.stdin.readline())
for _ in range(Q):
    x = int(sys.stdin.readline())
    print(subsize[x - 1])

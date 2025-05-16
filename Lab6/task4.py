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

def set_parent(adj, r, parent):
    # if len(adj[r]) <= 1:
    #     return
    
    for c in adj[r]:
        if c == parent[r] :
            continue
        else:
            parent[c] = r
            set_parent(adj, c, parent)

def find_subT(u, adj, parent):
    if len(adj[u]) <= 1:
        sub_trees[u] = 1
        return 1
    subs = 1
    for v in adj[u]:
        # subs = 1
        if v != parent[u]:
            subs += find_subT(v, adj, parent)
    sub_trees[u] = subs
    return subs

V, R = map(int, input().split())
adj = make_adj(V)
# print(adj)

par = [None]*V
par[R-1] = -1
set_parent(adj, R-1, par)
# print(par)

sub_trees = [0]*V
find_subT(R-1, adj, par)

qs = int(input())
for i in range(qs):
    r = int(input())
    # print(find_subT(r-1, adj, par))
    print(sub_trees[r-1])


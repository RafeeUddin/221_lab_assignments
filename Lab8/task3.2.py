class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def dfs_strictly_smaller(u, v, limit, adj, vis, stamp):
    stack = [(u, -1)]
    while stack:
        node, max_below = stack.pop()
        if node == v:
            return max_below
        if vis[node] == stamp:
            continue
        vis[node] = stamp
        for nei, w in adj[node]:
            if vis[nei] != stamp:
                best = max_below
                if w < limit and w > max_below:
                    best = w
                stack.append((nei, best))
    return -1

def secondMST(n, edges):
    edges.sort()
    dsu = DSU(n)
    mst_cost = 0
    adj = [[] for _ in range(n)]
    used = [False] * len(edges)

    for i, (w, u, v) in enumerate(edges):
        if dsu.unite(u, v):
            used[i] = True
            mst_cost += w
            adj[u].append((v, w))
            adj[v].append((u, w))

    if sum(used) != n - 1:
        return -1

    vis = [0] * n
    stamp = 1
    res = float('inf')

    for i, (w, u, v) in enumerate(edges):
        if used[i]:
            continue
        stamp += 1
        smaller = dfs_strictly_smaller(u, v, w, adj, vis, stamp)
        if smaller != -1:
            new_cost = mst_cost - smaller + w
            if new_cost > mst_cost:
                res = min(res, new_cost)

    return -1 if res == float('inf') else res

# Input handling
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))

print(secondMST(n, edges))
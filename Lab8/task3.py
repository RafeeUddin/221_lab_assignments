from collections import deque
import heapq

def get_rep(u):
    if rep[u] != u:
        rep[u] = get_rep(rep[u])
    return rep[u]

V, E = map(int, input().split())
rep = [i for i in range(V+1)]
size = [1 for j in range(V+1)]
h = []
mst1 = 0
not_in_mst1 = deque()
for e in range(E):
    s, d, w = map(int, input().split())
    heapq.heappush(h, (w, s, d))
in_mst = []

while h:
    w, s, d = heapq.heappop(h)
    rep_u, rep_v = get_rep(s), get_rep(d)

    if rep_u != rep_v:
        if size[rep_u] < size[rep_v]:
            rep_v, rep_u = rep_u, rep_v
        size[rep_u] += size[rep_v]
        rep[rep_v] = rep_u
        mst1 += w
        heapq.heappush(in_mst, (w, s, d))
    else:
        not_in_mst1.append((w, s, d))

# print(mst1)
# print(not_in_mst1)
# print(in_mst)

def pr_mst(ex, in_mst):

    def get_rep(u):
        if rep[u] != u:
            rep[u] = get_rep(rep[u])
        return rep[u]

    rep = [i for i in range(V+1)]
    size = [1 for j in range(V+1)]
    t_mst1 = []
    wx, sx, dx = ex
    cst = wx
    rep[dx] = rep[sx]
    size[sx] += size[dx]
    # print(in_mst)

    while in_mst:
        w2, s2, d2 = heapq.heappop(in_mst)
        # print(s2, d2)
        heapq.heappush(t_mst1, (w2, s2, d2))
        rep_u2, rep_v2 = get_rep(s2), get_rep(d2)
        # print(rep_u2, rep_v2)

        if rep_u2 != rep_v2:
            if size[rep_u2] < size[rep_v2]:
                rep_v2, rep_u2 = rep_u2, rep_v2
            size[rep_u2] += size[rep_v2]
            rep[rep_v2] = rep_u2
            cst += w2

    # print(rep, size)
    return (cst, t_mst1)


mst2 = []
while not_in_mst1:
    ex = not_in_mst1.popleft()

    mstx, in_mst = (pr_mst(ex, in_mst))
    if mstx != mst1:
        mst2.append(mstx)
print(min(mst2))
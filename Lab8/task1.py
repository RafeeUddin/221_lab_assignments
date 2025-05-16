from collections import deque

def get_rep(u):
    if rep[u] == u:
        return u
    else:
        return get_rep(rep[u])
    
V, E = map(int, input().split())
rep = [i for i in range(V+1)]
# friends = {j: {j} for j in range(1, V+1)}
size = [1 for j in range(V+1)]

q = deque()
for e in range(E):
    s,d = map(int, input().split())
    q.append((s, d))

# print(rep)
# print(friends)

while q:

    u, v = q.popleft()
    rep_u, rep_v = get_rep(u), get_rep(v)
    # print(rep_u, rep_v)

    # if rep_u == rep_v:
    #     print(len(friends[rep_u]))
    #     # continue
    # else:
    #     friends[rep_u] = friends[rep_u].union(friends[rep_v])
    #     rep[rep_v] = rep_u
    #     print(len(friends[rep_u]))
    
    if rep_u != rep_v:
        if size[rep_u] < size[rep_v]:
            rep_u, rep_v = rep_v, rep_u
        rep[rep_v] = rep_u
        size[rep_u] += size[rep_v]
    print(size[rep_u])
    # print(rep)
    # print(friends)
        
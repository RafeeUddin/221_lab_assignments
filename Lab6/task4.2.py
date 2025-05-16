import sys
sys.setrecursionlimit(2*100000+5)
from collections import deque

N, R = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(N-1):
    s, e = map(int, input().split())
    adj[s-1].append(e-1)
    adj[e-1].append(s-1)

sub_size = [0]*N
visit = [0]*N
stk = deque()
order = []

# visit[R-1] = 1
# sub_size[R-1] = 1
stk.append((R-1, -1))

while stk:
    u, p = stk.pop()
    visit[u] = 1
    order.append((u, p))
    for v in adj[u]:
        if v != p:
            stk.append((v, u))

order = reversed(order)
for i, j in order:
    sub_size[i] = 1
    for k in adj[i]:
        if k != j:
            sub_size[i] += sub_size[k]
    # if j != -1:
    #     sub_size[j] += sub_size[i]


# def get_subsize(adj, sub_size, u, p):

#     sub_size[u] = 1
#     visit[u] = 1
#     for v in adj[u]:
#         if v == p:
#             continue
#         else:
#             get_subsize(adj, sub_size, v, u)
#             sub_size[u] += sub_size[v]


# get_subsize(adj, sub_size, R-1, -1)

query = int(input())
for _ in range(query):
    print(sub_size[int(input())-1])
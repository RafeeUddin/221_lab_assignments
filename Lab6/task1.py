import sys
sys.setrecursionlimit(2*100000+5)

def make_adj (N, M):
    # print(N, M)
    adj = [[]]
    for n in range(N):
        adj.append([])
    # print(adj)
    for m in range(M):
        s,e = list(map(int, (input().split())))
        adj[s-1].append(e)

    return adj


def visit(n, adj, color, order):
    x = 1
    color[n] = 1
    for i in adj[n]:
        if color[i-1] == 1:
            x = -1
        if color[i-1] == 0:
            x = visit(i-1, adj, color, order)
        if x == -1:
            return x
    
    color[n] = 2
    order.append(n)

N,M = list(map(int, (input().split())))
# print(N, M)
adj = make_adj(N,M)
color = [0]*N
order = []
x = 1
for n in range(N):
    if color[n] == 0:
        x = visit(n, adj, color, order)
    if x == -1 and len(order) != N:
        # print(order)
        print("-1")
        break
    if len(order) == N:
        break
    # if n not in order:
    #     order.append(n)
    # print(order)

if x != -1:
    print(" ".join(map(str, map(lambda x: x+1, list(reversed(order))))))
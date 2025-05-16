from collections import deque
import sys
sys.setrecursionlimit(2*100000+5)

V, E, S, D, K = list(map(int, input().split()))
adj_lst = [None]*V
for a in range(V):
    adj_lst[a] = []
if E != 0:
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
for a in range(E):
    adj_lst[start[a]-1].append(end[a])
    adj_lst[end[a]-1].append(start[a])
for each in adj_lst:
    each.sort()

color = [0]*V
parent = [-1]*V
Q = deque()

Q.append(S)
# parent[S-1] = -1
color[S-1] = 1
while len(Q)  != 0:
    u = Q.popleft()
    for v in adj_lst[u-1]:
        if color[v-1] == 0:
            Q.append(v)
            color[v-1] = 1
            parent[v-1] = u

if S == D:
    print(0)
    print(S)

cur = D-1
to_print = [D]
cnt = 0
while parent[cur] != -1:
    if parent[cur] == S:
        to_print.append(parent[cur])
        cnt += 1
        break
    to_print.append(parent[cur])
    cnt += 1
    cur = parent[cur]-1

# print(to_print)
if S != D:
    if cnt != 0:
        print(cnt)
        for i in range(1, len(to_print)):
            print(to_print[len(to_print)-i], end=" ")
        print(to_print[0])
    else:
        print(-1)

# print(color)
# print(parent)
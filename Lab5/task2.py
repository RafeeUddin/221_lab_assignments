import sys
sys.setrecursionlimit(2*100000+5)

def DFS(adj_lst, color, to_print):
    for i in range(len(adj_lst)):
        if color[i] == 0:
            DFS_visit(adj_lst, i, color, to_print)

def DFS_visit(adj_lst, i, color, to_print):
    color[i] = 1
    to_print.append(i+1)
    # print(to_print)
    for j in adj_lst[i]:
        # print(i, j)
        # if color[adj_lst[i][j-1]-1] == 0:
        if color[j-1] == 0:
            DFS_visit(adj_lst, j-1, color, to_print)
    color[i] = 2


V, E = list(map(int, input().split()))
adj_lst = [None]*V
for a in range(V):
    adj_lst[a] = []
color = [0]*V
start = list(map(int, input().split()))
end = list(map(int, input().split()))
for a in range(E):
    adj_lst[start[a]-1].append(end[a])
    adj_lst[end[a]-1].append(start[a])

# print(adj_lst)
# for i in range(E):
#     st, en = list(map(int, input().split()))
#     adj_lst[st-1].append(en)
#     adj_lst[en-1].append(st)

to_print = []
DFS(adj_lst, color, to_print)
print(" ".join(list(map(str, to_print))))

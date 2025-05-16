nodes = int(input())
adj_mat = []

for i in range(nodes):
    adj_mat.append([0]*nodes)

for n in range(nodes):
    each = list(map(int, input().split()))
    for e in range(each[0]):
        adj_mat[n][each[e+1]] = 1
        adj_mat[each[e+1]][n] = 1

for j in range(nodes):
    print(" ".join(map(str, adj_mat[j])))
# print(adj_mat)


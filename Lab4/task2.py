nodes, edges = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list(map(int, input().split()))
weight = list(map(int, input().split()))

Nodes = []
for n in range(nodes):
    Nodes.append([])

for e in range(edges):
    Nodes[start[e]-1].append((end[e], weight[e]))

for i in range(len(Nodes)):
    print(f"{i+1}:", end=" ")
    for j in range(len(Nodes[i])):
        print(Nodes[i][j], end=" ")
    print() 
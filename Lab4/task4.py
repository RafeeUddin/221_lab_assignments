N, E = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list(map(int, input().split()))

Nodes = [0]*N

for i in range(E):
    Nodes[start[i]-1] += 1
    Nodes[end[i]-1] += 1

odd = 0
for j in range(N):
    if Nodes[j]%2 != 0:
        odd += 1
    
if odd == 2 or odd == 0:
    print("YES")
else:
    print("NO")
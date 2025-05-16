def gcd(x,y):
    while y!=0:
        x, y = y, x%y
    return x == 1

size, query = list(map(int, input().split()))
vert = []

for i in range(1, size+1):
    temp = []

    for j in range(1, size+1):
        if gcd(i, j) and i!=j:
            temp.append(j)

    vert.append(temp)

# print(vert)
for k in range(query):
    v, n = list(map(int, input().split()))
    if n <= len(vert[v-1]):
        print(vert[v-1][n-1])
    else:
        print("-1")
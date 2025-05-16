hh = []
hh.append((2,3))
hh.append((5,5))
print(hh)

def gcd(x,y):
    while y!=0:
        x, y = y, x%y
    return x == 1

vert = []
for i in range(1, 5+1):
    temp = []
    for j in range(1, 5+1):
        if gcd(i, j) and i!=j:
            temp.append(j)
    vert.append(temp)
print(vert)
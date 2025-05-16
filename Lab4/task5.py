V, E = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list(map(int, input().split()))

vertices = [0]*V
for e in range(E):
    vertices[start[e]-1] -= 1
    vertices[end[e]-1] += 1

print(" ".join(map(str, vertices)))
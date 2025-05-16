
n = int(input())
arr = list(map(int, input().split()))

i, j = 0, 1
max_sum = -1

while j<n:
    max_sum = max(max_sum, (arr[i]+arr[j]**2))
    if arr[i] < arr[j]:
        i = j
    j += 1
    
print(max_sum)
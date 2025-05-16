size = int(input())
# arr1 = input().split()
arr1 = list(map(int, input().split()))

for i in range(size-1):
    sorted = True
    for j in range(size-1-i):
        # arr1[j], arr1[j+1] = int(arr1[j]), int(arr1[j+1])
        if arr1[j] > arr1[j+1]:
            sorted = False
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
    # print(arr1)
    if sorted == True:
        break
    # print(arr1)

for i in range(size-1):
    print(arr1[i], end=" ")
print(arr1[size-1])
# print(arr1)
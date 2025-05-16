def binary_tree(arr, start, end, result):
    if start > end:
        return
    mid = (start+end)//2
    result.append(arr[mid])

    binary_tree(arr, start, mid-1, result)
    binary_tree(arr, mid+1, end, result)
    
result = []
n = int(input())
arr = list(map(int, input().split()))
binary_tree(arr, 0, len(arr)-1, result)
print(" ".join(list(map(str, result))))
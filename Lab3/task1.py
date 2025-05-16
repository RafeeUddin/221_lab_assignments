def mergeSort(arr, start, end, count):
    if start >= end:
        return arr[start:end+1], count
    
    mid = (start + end)//2
    
    left, count = mergeSort(arr, start, mid, count)
    right, count = mergeSort(arr, mid+1, end, count)
    merged, count = merge(left, right, count)
    return merged, count

def merge(left, right, count):
    i, j = 0, 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            count += len(left)-i
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1
    return temp, count

count = 0
size = int(input())
arr = list(map(int, input().split()))
sorted, count = mergeSort(arr, 0, len(arr)-1, count)
print(count)
for i in range(len(sorted)):
    if i < len(sorted):
        print(sorted[i], end = " ")
    else:
        print(sorted[i])
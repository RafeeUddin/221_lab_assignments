def find_numbers(lst, start, end, ):
    l,r = 0, len(lst)
    while l<r:
        mid = (l+r)//2
        
        if lst[mid]<start:
            l = mid+1
        else:
            r = mid
    left = l

    l,r = 0, len(lst)
    while l<r:
        mid = (l+r)//2

        if lst[mid]<=end:
            l = mid+1
        else:
            r = mid
    right = l
    return(right-left)
        

size, tests = list(map(int, input().split()))
lst = list(map(int, input().split()))

for i in range(tests):
    start, end = list(map(int, input().split()))
    print(find_numbers(lst, start, end))

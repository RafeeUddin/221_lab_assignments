

def chksm():
    size, req_sum = list(map(int, input().split()))
    digits = list(map(int, input().split()))

    i, j = 0, size-1
    sum = 0
    while i < j:
        sum = digits[i]+digits[j]
        if sum == req_sum:
            print(i+1,j+1)
            return
        elif sum < req_sum:
            i+=1
        elif sum > req_sum:
            j-=1
    print(-1)     

chksm()
def fastMod(a,b,m=107):
    if b == 1:
        return a%m
    elif b>1:
        if b%2 == 0:
            ret = fastMod(a, b/2, m)**2
            
        else:
            left = fastMod(a, b-1, m)
            right = fastMod(a, 1, m)
            ret = left*right
            
        if ret >= m:
            return ret%m
        return ret
        
a, b = list(map(int, input().split()))
print(fastMod(a,b))
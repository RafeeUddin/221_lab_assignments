def fastMod(a,b,m):
    result = 1
    modded = a%m
    while b>0:
        if b%2 == 1:
            result = (modded*result)%m
        modded = (modded**2)%m
        b = b//2
    return result
        

def fastModRev(a, n, m):
    if n == 1:
        return a%m
    
    if n%2 != 0:
        odd_to_even = fastModRev(a, n-1, m)
        A = (odd_to_even + fastMod(a,n,m)) % m
        return A
    else:
        half_sum = fastModRev(a, n//2, m)
        A = (half_sum*(1+fastMod(a,n//2,m))) %m
        return A

tests = int(input())
for i in range(tests):
    a, n , m = list(map(int, input().split()))
    result = fastModRev(a, n, m)
    print(int(result))
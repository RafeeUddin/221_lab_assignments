def fastModRev(a, n, m):
    if n == 1:
        return a%m
    
    if n%2 != 0:
        odd_to_even = fastModRev(a, n-1, m)
        return (odd_to_even + pow(a,n,m)) % m
    else:
        half_sum = fastModRev(a, n//2, m)
        return (half_sum*(1+pow(a,n//2,m))) % m


tests = int(input())
for i in range(tests):
    a, n , m = list(map(int, input().split()))
    result = fastModRev(a, n, m)
    print(int(result))
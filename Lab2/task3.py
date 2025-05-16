import io, sys, os

size, find = list(map(int, input().split()))
nums = list(map(int, input().split()))
# nums = list(map(int, sys.stdin.readline().split()))
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# nums = list(map(int, input().decode().split()))
# nums = list(map(int, sys.stdin.readline().split()))

# print(nums)

i,j = 0,0
max_len, sums = 0, 0
while j < size and i < size:
    sums += nums[j]

    if sums <= find:
        max_len = max(max_len, j-i+1)
    else:
        sums -= nums[i]
        i += 1
    j += 1

print(max_len)
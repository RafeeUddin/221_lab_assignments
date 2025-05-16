sizes = input()
array_size, reversal_size = sizes.split(" ")
# print(array_size, reversal_size)
arr1 = input().split()

for j in range(int(reversal_size)):
    print(arr1[int(reversal_size) - 1 - j], end = " ")
    
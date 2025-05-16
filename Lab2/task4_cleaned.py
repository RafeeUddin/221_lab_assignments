def find_1st_1(bin_str, left, right):
    
    first = -1
    
    while left <= right:
        mid = (left + right)//2

        if bin_str[mid] == "1":
            first = mid+1
            right = mid-1
        else:
            left = mid+1

    return first

total_inputs = int(input())

for i in range(total_inputs):
    bin_str = input()

    left, right = 0, len(bin_str)-1
    first_1 = find_1st_1(bin_str, left, right)
    print(first_1)
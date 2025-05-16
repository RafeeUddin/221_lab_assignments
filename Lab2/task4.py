def find_1st_1(bin_str, left, right):
    
    # left, right = left, right
    # mid = int((left + right)/2)
    
    # # if len(bin_str) == 1:
    # #     if bin_str[0] == "1":
    # #         return 1
    # #     else:
    # #         return -1
        
    # if bin_str[mid] == "1":
    #     if mid == 0:
    #         return mid+1
    #     elif bin_str[mid-1] == "1":
    #         return find_1st_1(bin_str, left, mid-1)
    #     else:
    #         return mid+1
    # else:
    #     if mid == len(bin_str)-1:
    #         return -1
    #     elif bin_str[mid+1] == "1":
    #         return mid+2
    #     else:
    #         return find_1st_1(bin_str, mid+1, right)
        

    if left == len(bin_str)-2:
        return -1
    
    mid = (left + right)//2
    
    if bin_str[mid] == "1":
        if mid == 0 or bin_str[mid-1] == "0":
            return mid+1
        else:
            return find_1st_1(bin_str, left, mid-1)
        
    else:
        return find_1st_1(bin_str, mid+1, right)
        
        
test_input = open("Lab2/task4_input.txt", "r")
total_inputs = int(test_input.readline())
# total_inputs = int(input())

for i in range(total_inputs):
    # bin_str = input()
    bin_str = str(test_input.readline())
    print(f"line {i} is {bin_str} of size {len(bin_str)}")

    left, right = 0, len(bin_str)-1
    first_1 = find_1st_1(bin_str, left, right)
    print(first_1)

test_input.close
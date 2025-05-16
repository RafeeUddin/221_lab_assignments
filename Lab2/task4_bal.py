def find_1st_1(bin_str, left, right):
    
    if left > right:
        return -1
    mid = (left + right)//2
    
    if bin_str[mid] == "1":
        if mid == 0 or bin_str[mid-1] == "0":
            return mid+1
        else:
            return find_1st_1(bin_str, left, mid-1)
        
    else:
        return find_1st_1(bin_str, mid+1, right)
        

# total_inputs = int(input())
test_input = open("Lab2/task4_input.txt", "r")
total_inputs = int(test_input.readline())

for i in range(total_inputs):
    # bin_str = input()
    bin_str = str(test_input.readline())
    # print(f"line {i} is {bin_str} of size {len(bin_str)}")

    left, right = 0, len(bin_str)-1
    first_1 = find_1st_1(bin_str, left, right)
    print(first_1)

test_input.close

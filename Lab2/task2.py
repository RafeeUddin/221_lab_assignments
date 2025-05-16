lst_a_len = int(input())
lst_a = list(map(int, input().split()))
lst_b_len = int(input())
lst_b = list(map(int, input().split()))

a, b = 0, 0
merged_lst = []
while a < lst_a_len and b < lst_b_len:
    if lst_a[a] < lst_b[b]:
        merged_lst.append(lst_a[a])
        a += 1
    else:
        merged_lst.append(lst_b[b])
        b += 1

if a == lst_a_len:
    merged_lst.extend(lst_b[b:])
if b == lst_b_len:
    merged_lst.extend(lst_a[a:])

# print(lst_a)
# print(lst_b)
# print(merged_lst)

for i in range(len(merged_lst)):
    if i == len(merged_lst)-1:
        print(merged_lst[i])
    else:
        print(merged_lst[i], end = " ")
    
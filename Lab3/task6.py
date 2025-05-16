def post_it_up(pre_ord, in_ord):
    size = len(pre_ord)
    if size <= 1:
        return pre_ord
    pre_1st = pre_ord[0]
    for i in range(size):
        if in_ord[i] == pre_1st:
            in_ind = i
            break
    post_left = post_it_up(pre_ord[1:1+in_ind], in_ord[0:in_ind])
    # print(post_left)
    post_right = post_it_up(pre_ord[1+in_ind:], in_ord[in_ind+1:])
    # print(post_right)
    post = post_left+post_right+[pre_1st]

    return post

size = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))
post_order = post_it_up(pre_order, in_order)
print(" ".join(list(map(str, post_order))))
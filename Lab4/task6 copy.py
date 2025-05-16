size = int(input())
px, py = list(map(int, input().split()))
valid = []

if px == 1 and py == 1 and size != 1:
    valid.append((1, 2))
    valid.append((2, 1))
    valid.append((2, 2))

elif px == 1 and py == size and size != 1:
    valid.append((1, size-1))
    valid.append((2, size-1))
    valid.append((2, size))

elif px == size and py == 1 and size != 1:
    valid.append((size-1, 1))
    valid.append((size-1, 2))
    valid.append((size, 2))

elif px == size and py == size and size != 1:
    valid.append((size-1, size-1))
    valid.append((size-1, size))
    valid.append((size, size-1))

else:

    # if px-1 <= 0 :
    #     pass
    # else:
    if px-1 > 0:
        if py-1 > 0:
            valid.append((px-1, py-1))
        valid.append((px-1, py))
        if py+1 <= size:
            valid.append((px-1, py+1))

    # if py-1 <= 0:
    #     pass
    # else:
    if py-1 > 0:
        valid.append((px, py-1))

    # if py+1 > size:
    #     pass
    # else:
    if py+1 <= size:
        valid.append((px, py+1))
        
    # if px+1 > size:
    #     pass
    # else:
    if px+1 <= size:
        if py-1 > 0:
            valid.append((px+1, py-1))
        valid.append((px+1, py))
        if py+1 <= size:
            valid.append((px+1, py+1))

print(len(valid))
for each in valid:
    print(f"{each[0]} {each[1]}")
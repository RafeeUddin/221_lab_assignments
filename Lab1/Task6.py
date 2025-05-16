size = int(input())
tuples = []
ids = input().split(" ")
score = input().split(" ")
for i in range(size):
    tuples.append([int(ids[i]), int(score[i])])
# print(tuples)

swaps = 0

for i in range(size-1):
    top = i
    for j in range(i+1, size):
        if tuples[j][1] > tuples[top][1]:
            top = j
        elif tuples[j][1] == tuples[top][1]:
            if tuples[j][0] < tuples[top][0]:
                top = j
    if top is not i:
        tuples[i], tuples[top] = tuples[top], tuples[i]
        swaps += 1
    
print(f"Minimum swaps: {swaps}")
for i in range(size):
    print(f'ID: {tuples[i][0]} Mark: {tuples[i][1]}')
# print(tuples)


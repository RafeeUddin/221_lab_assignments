# test inputs
# lines = 8
# trains_input = open("Task7_input.txt", "rt")
# for i in range(lines):
#     print(trains_input.readline(), end="")
# print()
# trains_input.close()
# 

class Trains:
    def __init__(self, name, dest, time):
        self.name = name
        self.dest = dest
        self.time = time
        self.this_train = [self.name, self.dest, self.time]

num_of_trains = int(input())
train_list = []
trains_input = open("Task7_input.txt", "rt") #file theke input text korar jonno
for i in range(num_of_trains):
    # splits = input().split()
    thisLine = trains_input.readline() #eta file theke input naoar jonno 
    splits = thisLine.split() #same as above
    # print(splits)
    name, dest, time = splits[0], splits[4], splits[6]
    train_list.append(Trains(name,dest,time))
    # print(train_list[i].this_train)
trains_input.close()

# this block is for selection sorting

# for i in range(num_of_trains-1):
#     top = i
#     for j in range(i+1, num_of_trains-1):
#         if train_list[j].name < train_list[top].name:
#             top = j
#         if train_list[j].name == train_list[top].name:
#             if train_list[j].time > train_list[top].time:
#                 top = j
#     if top != i:
#         train_list[top], train_list[i] = train_list[i], train_list[top]


for i in range(num_of_trains-1):
    for j in range(num_of_trains-1-i):
        if train_list[j].name > train_list[j+1].name:
            train_list[j], train_list[j+1] = train_list[j+1], train_list[j]
        elif train_list[j].name == train_list[j+1].name:
            if train_list[j].time < train_list[j+1].time:
                train_list[j], train_list[j+1] = train_list[j+1], train_list[j]

# for i in range(num_of_trains): 
#     print(train_list[i].this_train)
for i in range(num_of_trains):
    print(f"{train_list[i].name} will departure for {train_list[i].dest} at {train_list[i].time}")
    

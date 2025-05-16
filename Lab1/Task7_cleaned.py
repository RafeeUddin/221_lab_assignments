class Trains:
    def __init__(self, name, dest, time, serial):
        self.name = name
        self.dest = dest
        self.time = time
        self.serial = serial
        self.this_train = [self.name, self.dest, self.time, self.serial]

num_of_trains = int(input())
train_list = []

for i in range(num_of_trains):
    splits = input().split()
    name, dest, time, serial = splits[0], splits[4], splits[6], i
    train_list.append(Trains(name,dest,time,serial))

for i in range(num_of_trains-1):
    top = i
    for j in range(i+1, num_of_trains-1):
        if train_list[j].name < train_list[top].name:
            top = j
        if train_list[j].name == train_list[top].name:
            if train_list[j].time > train_list[top].time:
                top = j
            elif train_list[j].time == train_list[top].time:
                if train_list[j].serial < train_list[top].serial:
                    top = j
    if top != i:
        train_list[top], train_list[i] = train_list[i], train_list[top]

for i in range(num_of_trains):
    print(f"{train_list[i].name} will departure for {train_list[i].dest} at {train_list[i].time}")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == None:
            return True
        
    def enque(self, v):
        nn = Node(v)
        if self.isEmpty():
            self.front = self.rear = nn
            return
        self.rear.next = nn
        self.rear = nn

    def deque(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data 


V, E = list(map(int, input().split()))
adj_lst = [None]*V
for a in range(V):
    adj_lst[a] = []
color = [0]*V
for i in range(E):
    st, en = list(map(int, input().split()))
    adj_lst[st-1].append(en)
    adj_lst[en-1].append(st)
# print(adj_lst)

Q = Queue(V)
Q.enque(1)
to_print = [1]
color[1-1] = 1
while not Q.isEmpty():
    deq = Q.deque()
    for each in (adj_lst[deq-1]):
        if color[each-1] == 0:
            Q.enque(each)
            color[each-1] = 1
            to_print.append(each)
            # print(to_print)

print(" ".join(list(map(str, to_print))))
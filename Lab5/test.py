from collections import deque

adj = [[]]*2
print(adj)

asc = [9]
asc.append(3)
print(asc)

dd = [4, [3, 2], [5, 3, 6]]
print(len(dd))

q = deque()
q.append(4)
q.append(6)
q.append(1)
print(min(q))
h = deque()
h.append("ad")
print(h)
print(q)
q.remove(1)
print(q)
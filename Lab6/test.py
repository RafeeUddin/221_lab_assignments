# order = [5, 6, 2, 1, 0]
# orr = list(reversed(order))
# print(orr)

# dic = {'k': (4, 't'), 'g': (14, 'h')}
# print(max(dic, key = dic.get))

# jj = {'0':1, '4':1}
# print((max(jj.items())))
# jj[max(jj, key=jj.get)] += 1
# print(jj)
# print(int(max(jj, key=jj.get)))
# print(jj)

# ss = []
# for i in range(3):
#     ss.append(set())
# print(ss)
# ss[1].add(33)
# print(ss)

# adj = {}
# st = "3"
# for new in range(4):

#     if st not in adj:
#         adj[st] = {new}
#     else:
#         adj[st].add(new)
# print(adj)

s, d = map(int, input().split())
print(s, d)
print(type(s))
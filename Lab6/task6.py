from collections import deque
import heapq

N = int(input())
adj = {}
words = []
indegree = {}
valid = True

for i in range(N):
    word = input()
    words.append(word)
    for ch in word:
        if ch not in adj.keys():
            adj[ch] = []
            indegree[ch] = 0

for j in range(N-1):
    w1 = words[j]
    w2 = words[j+1]
    small = min(len(w1), len(w2))
    error = False

    for k in range(small):
        if w1[k] != w2[k]:
            if w2[k] not in adj[w1[k]]:
                adj[w1[k]].append(w2[k])
                indegree[w2[k]] += 1
            error = True
            break
    
    if not error and len(w1) > len(w2):
        print(-1)
        valid = False
        break

if valid:
    min_heap = []
    for ch in adj:
        if indegree[ch] == 0:
            heapq.heappush(min_heap, ch)

    order = ""
    while min_heap:
        cur = heapq.heappop(min_heap)
        order += cur
        for u in adj[cur]:
            indegree[u] -= 1
            if indegree[u] == 0:
                heapq.heappush(min_heap, u)

    if len(order) != len(adj):
        print(-1)
    else:
        print(order)
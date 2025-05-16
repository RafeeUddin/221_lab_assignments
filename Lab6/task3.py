from collections import deque

N = int(input())
xi, yi, xf, yf = list(map(int, input().split()))

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
q = deque()
color = [0]*(N*N)
parent = [None]*(N*N)
time = [float("inf")]*(N*N)
t = 1

start = ((xi-1)*N)+(yi-1)
end = ((xf-1)*N)+(yf-1)

q.append(start)
color[start] = 1
time[start] = t
t += 1
while q:
    curr = q.popleft()
    
    xc, yc = divmod(curr, N)
    for x, y in moves:
        if 0<= xc+x < N and 0<= yc+y < N:
            new = (xc+x)*N + (yc+y)
            if t<time[new]:
                q.append(new)
                
                color[new] = 1
                time[new] = t
                parent[new] = curr
    color[curr] = 2
    t += 1
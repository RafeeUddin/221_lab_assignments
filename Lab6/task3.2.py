from collections import deque

N = int(input())
sx, sy, ex, ey = map(int, input().split())

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

clr = [[0]*(N+1) for _ in range(N+1)]
step = [[0]*(N+1) for _ in range(N+1)]

q = deque()
q.append((sx, sy))
clr[sx][sy] = 1
path = False

while q:
    cx, cy = q.popleft()

    if (cx, cy) == (ex, ey):
        print(step[cx][cy])
        path = True
        break

    for x, y in moves:
        nx, ny = cx+x, cy+y

        if 0< nx <=N and 0 < ny <= N:
            if clr[nx][ny] == 0:
                clr[nx][ny] = 1
                step[nx][ny] = step[cx][cy] + 1
                q.append((nx, ny))

if path == False:
    print(-1)
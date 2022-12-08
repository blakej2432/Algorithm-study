import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

a, b, c, d = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append([0]*N)

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[c][d]

print(bfs(a, b))



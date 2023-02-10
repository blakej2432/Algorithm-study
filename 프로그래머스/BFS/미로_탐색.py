# pseudo code
'''
단순 bfs 최단경로 찾기 문제
네 방향으로 이동 경우 중 1인 경우에만 이동 하며 이전까지의 거리에 +1
찾고자 하는 위치에 도달하면 return
'''

# my code
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

miro = []

for _ in range(N):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(miro):
    queue = deque([(0,0)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0 and miro[ny][nx] == 1:
                visited[ny][nx] = 1
                miro[ny][nx] = miro[y][x] + 1
                queue.append((ny, nx))

                if ny == N-1 and nx == M-1:
                    return miro[ny][nx]


print(bfs(miro))

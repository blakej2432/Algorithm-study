# 게임 맵 최단거리
# 문제 설명
# ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

# 지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예


from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    def bfs(x,y):
        n = len(maps[0])
        m = len(maps)
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        return maps[n-1][m-1]
    answer = bfs(0,0)
    return -1 if answer == 1 else answer

# x, y랑 n,m 관계 잘 확인해 어디가 가로고 어디가 세로고
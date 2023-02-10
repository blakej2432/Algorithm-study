# pseudo code
'''
특정 점에서 점까지 거리를 구해야 하므로 bfs 이용
지나갈 필요가 없는 점 'X'를 마주치면 거리를 판단하는 조건 자체를 걸지 않는다.
일반적인 최단거리 구하기는 start점이 고정이지만 여기선 P에 따라 여러 start점을 설정하고 시작
길이가 2가 되기전에 다른 'P'를 마주치면 종료
'''


# my code
from collections import deque

def bfs(place):
    P_seat = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                P_seat.append([i, j])
                
    for P in P_seat:
        queue = deque([P])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[P[0]][P[1]] = 1
        
        while queue:
            y, x = queue.popleft()
            
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if place[ny][nx] == '0':
                        visited[ny][nx] = 1
                        queue.append([ny, nx])
                        distance[ny][nx] = distance[y][x] + 1
                        
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
                       
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
        
    return answer   
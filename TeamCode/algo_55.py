# 바이러스 DFS

import sys

k = int(sys.stdin.readline().rstrip())

graph =[[] for i in range(k+1)]

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

visited = [False] * (k+1)

answer = []
def dfs(graph, v, visited):
    visited[v] = True
    answer.append(v)
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(len(answer) - 1)

# 바이러스 BFS

import sys
from collections import deque
k = int(sys.stdin.readline().rstrip())

graph =[[] for i in range(k+1)]

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

visited = [False] * (k+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



bfs(graph, 1, visited)
print(len(answer) - 1)









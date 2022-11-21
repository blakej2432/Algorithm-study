# 숨바꼭질 3

import sys
from collections import deque

MAX = 100001
n, k = map(int, sys.stdin.readline().split())
visited = [False] * MAX
second = [0] * MAX
visited[n] = True

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return second[v]

        for next_v in [2*v, v-1, v+1]:
            if next_v == 2*v and 0 <= next_v < MAX and not visited[next_v]:
                q.append(next_v)
                second[next_v] = second[v]
                visited[next_v] = True


            if (next_v == v-1 or next_v == v+1) and 0 <= next_v < MAX and not visited[next_v]:
                q.append(next_v)
                second[next_v] = second[v] + 1
                visited[next_v] = True
                
print(bfs())










# import sys
# from collections import deque

# MAX = 100001
# n, k = map(int, sys.stdin.readline().split())
# visited = [False] * MAX
# second = [-1] * MAX

# def bfs(v):
#     second[v] = 0
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if v == k:
#             return second[v]
#         if 0 <= v-1 < MAX and not visited[v-1]:
#             visited[v-1] = True
#             second[v-1] = second[v] + 1
#             q.append(v-1)
#         if 0 <= v+1 < MAX and not visited[v+1]:
#             visited[v+1] = True
#             second[v+1] = second[v] + 1
#             q.append(v+1)
#         if 0 <= 2*v < MAX and not visited[2*v]:
#             visited[2*v] = True
#             second[2*v] = second[v]
#             q.append(2*v)


# print(bfs(n))




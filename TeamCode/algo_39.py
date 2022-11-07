import sys

N, M = map(int, sys.stdin.readline().split())

N_friend = []
for i in range(N):
	N_friend.append(sys.stdin.readline().rstrip())

M_friend = []
for i in range(M):
	M_friend.append(sys.stdin.readline().rstrip())

friend_set = set(N_friend) & set(M_friend)

answer = sorted(list(friend_set))

if answer == []:
	print(-1)
else:
	for i in answer:
		print(i)
# mutual_lst = []
# for i in range(M):
# 	m = sys.stdin.readline().rstrip()
# 	if m in N_friend:
# 		mutual_lst.append(m)

# if mutual_lst == []:
# 	print(-1)
# else:
# 	for i in sorted(mutual_lst):
# 		print(i)


import sys

cnt_lst = [0]*4235
n, m, k = map(int, sys.stdin.readline().split())


for i in map(int, sys.stdin.readline().split()):
	cnt_lst[i] += 1 * 2


for i in map(int, sys.stdin.readline().split()):
	cnt_lst[i] += 1 * 3


for i in map(int, sys.stdin.readline().split()):
	cnt_lst[i] += 1
	
print(cnt_lst.index(max(cnt_lst)))


# merchant = list(map(int, sys.stdin.readline().split()))
# for i in merchant:
# 	cnt_lst[i] += 1 * 2

# nobility = list(map(int, sys.stdin.readline().split()))
# for i in nobility:
# 	cnt_lst[i] += 1 * 3

# citizen = list(map(int, sys.stdin.readline().split()))
# for i in citizen:
# 	cnt_lst[i] += 1
	
# print(cnt_lst.index(max(cnt_lst)))







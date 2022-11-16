import sys

total = sys.stdin.readline().split('-')

lst = []

for i in total:
    hap = 0
    plus = i.split('+')
    for j in plus:
        hap += int(j)
    lst.append(hap)

lst_1st = lst[0]
for i in range(1, len(lst)):
    lst_1st -= lst[i]
print(lst_1st)













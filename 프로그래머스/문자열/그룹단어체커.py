# pseudo code
'''
같은 알파벳이 연속으로 나올 경우는 상관없다.
같은 알파벳이 나왔으나, 연속으로 나온 것이 아닐 경우 그룹 단어가 아님 판정
위 경우에 해당 되지않고 loop가 끝나면 그룹단어 판정
'''

# my code
import sys
N = int(sys.stdin.readline().strip())

cnt = 0
for i in range(N):
    a = sys.stdin.readline().strip()
    g_word = True
    check = a[0]
    for j in range(1, len(a)):
        if a[j] not in check:
            check += a[j]
        elif a[j] in check and a[j] != a[j-1]:
            g_word = False
            break
    if g_word == True:
        cnt += 1

print(cnt)

# others'
'''
변수 할당 없이 문자열 자체에서 indexing으로 비교 가능하다
'''
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
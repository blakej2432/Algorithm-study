# 소수 찾기
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

from itertools import permutations

def solution(numbers):
    num = [i for i in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(permutations(num, i))

    case = [int(''.join(p)) for p in per]
    
    answer = []
    for i in case:
        if i < 2:
            continue
        check = True
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            answer.append(i)
    return len(set(answer))

# case에 숫자들 어떻게 처리했는지 확인, for문에서 소수 어떻게 찾았는지 확인
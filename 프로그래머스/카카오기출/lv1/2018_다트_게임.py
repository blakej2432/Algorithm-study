# pseudo code
'''
입력을 나눠줄 때, 정규표현식을 최대한 이용하자.
매 hit를 나눠서 저장하고, 각 hit 점수 계산
최종 점수를 점수 리스트에 저장
*, # 에 따라 이미 저장된 최종 점수 변경
'''

# my code
import re

def solution(dartResult):
    dartResult = re.findall('\d+\D*',dartResult)
    points = [0]
    
    for i in dartResult:
        num = int(re.findall('\d+', i)[0])
        
        if 'S' in i:
            points.append(num)
            
        if 'D' in i:
            num = num ** 2
            points.append(num)
            
        if 'T' in i:
            num = num ** 3
            points.append(num)
            
        if '*' in i:
            points[-2] = points[-2] * 2
            points[-1] = points[-1] * 2
        
        if '#' in i:
            points[-1] = -points[-1]
        
    return sum(points)

# others'
'''
dict로 문자를 처리해놓는다.
정규표현식을 더 자세히 (숫자, 보너스, 옵션)으로 표현 가능
'''
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

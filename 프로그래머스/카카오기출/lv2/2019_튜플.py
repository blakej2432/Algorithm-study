# pseudo code
'''
각 원소를 카운트 할 딕셔너리 생성
문자열에서 숫자가 등장할 때마다 딕셔너리의 value += 1
딕셔너리의 value기준 내림차순 정렬
정렬된 key값을 list로 변환
'''

# my code
from collections import defaultdict

def solution(s):
    dict_cnt = defaultdict(int)
    
    temp = ''
    for i in s:
        if i.isdigit():
            temp += i
        else:
            if temp != '':
                dict_cnt[temp] += 1
                temp = ''
            else:
                continue
            
    answer = sorted(dict_cnt.items(), key=lambda x : x[1] , reverse=True)
    answer = list(map(lambda x: int(x[0]), answer))
    return answer

# others'
'''
re.findall() 정규식으로 숫자 원소만 뽑아내기
defaultdict 선언 없이 Counter로 원소 세는 dict 바로 생성
list 내장객체로 map없이 원하는 값 뽑기
'''

import re
from collections import Counter

def solution(s):
    nums = re.findall('\d+', s)
    dict_cnt = Counter(nums)
    answer = [int(k) for k, v in sorted(dict_cnt.items(), key=lambda x : x[1], reverse=True)]
    
    return answer
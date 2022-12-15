# 파일명 정렬

import re

p = re.compile('([^0-9]+)([0-9]+)([\w\s]*)')

name_lst = []
def solution(files):
    for i in range(len(files)):
        name_lst.append((p.findall(files[i])[0],i))
    
    answer = []
    for i in range(len(files)):
        answer.append(files[sorted(name_lst, key = lambda x : (x[0][0].lower(), int(x[0][1])))[i][1]])
    return answer



# 다른 사람 풀이
a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
return b

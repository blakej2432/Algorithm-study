# pseudo code
'''
간단히 구현할 코드가 떠올랐더라도, 안되면 문제에서 하라는대로 무식하게 해보자
알파벳으로만 구성된 원소들 리스트에 저장
set변환 후 교집합, 합집합 원소들을 기존 리스트에서 .count하며 개수 세서 min, max 판단
'''


# my code
import re

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    elem_1 = []
    for i in range(len(str1)-1):
        if re.findall('[^a-zA-Z]+', str1[i:i+2]):
            continue
        else:
            elem_1.append(str1[i:i+2])
             
    elem_2 = []
    for i in range(len(str2)-1):
        if re.findall('[^a-zA-Z]+', str2[i:i+2]):
            continue
        else:
            elem_2.append(str2[i:i+2])
                   
    return J(elem_1, elem_2)

def J(A, B):
    
    if len(A) == 0 and len(B) == 0:
        return 1 * 65536
    
    else:
        inters = set(A) & set(B)
        unis = set(A) | set(B)

        J_inter = sum([min(A.count(inter), B.count(inter)) for inter in inters])
        J_uni = sum([max(A.count(uni), B.count(uni)) for uni in unis])      
    
        return int(J_inter/J_uni * 65536)
    
# others'
'''
알파벳 찾는거면 굳이 re.findall 안해도 .inalpha()로 찾으면 된다.
'''
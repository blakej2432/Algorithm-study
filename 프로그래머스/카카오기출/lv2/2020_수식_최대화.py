# pseudo code
'''
전체를 순열하는 건 시간 비효율적, 연산자의 순위만 순열
순열 리스트에서 하나씩 연산자를 기준으로 split하고 () 괄호와 함께 문자로 만들고 연산자로 join
문자열을 바로 계산하려면 eval()
최종값이 이전 값보다 크다면 answer 갱신
'''
# my code
from itertools import permutations

def solution(expression):
    answer = 0
    ops = ['+', '-', '*']
    
    for op in permutations(ops):
        fst, snd, trd = op[0], op[1], op[2]
        lst = []
        for i in expression.split(fst):
            temp = [f'({j})' for j in i.split(snd)]
            lst.append(f'({snd.join(temp)})')
        final = abs(eval(f'({fst.join(lst)})'))
        if final > answer:
            answer = final
            
    return answer

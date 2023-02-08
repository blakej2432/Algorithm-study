# pseudo code
'''
탐색할 때 리스트보다 dict가 더 빠르다. 이 접두사가 dict안에 있는지 확인한다.
for 문에서 해당 번호가 들어올 때 맨왼쪽부터 한숫자씩 접두사로 만든다.
접두사를 만들던 도중 그 접두사가 dict에 있다면 종료(단, 접두사가 현재 판단하는 번호와 일치하지 않을 때 조건)
'''


# my code
def solution(phone_book):
    answer = True
    num_dict = {}
    for i in phone_book:
        num_dict[i] = 1
    
    
    for i in phone_book:
        prefix = ""
        for j in i:
            prefix += j
            if prefix in num_dict and prefix != i:
                answer = False
        
    return answer
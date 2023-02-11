
# pseudo code
'''
이진법으로 각 지도 변환 후 해독 지도 생성
bina.rjust(n, '0') -> 오른쪽으로 밀어넣고 남은만큼 '0' 채우기

'''

# my code
def solution(n, arr1, arr2):
    map_1 = []
    for i in arr1:
        bina = format(i, 'b')
        if len(bina) < n:
            bina = bina.rjust(n, '0')
        map_1.append(bina)
        
    map_2 = []
    for i in arr2:
        bina = format(i, 'b')
        if len(bina) < n:
            bina = '0'*(n-len(bina)) + bina       
        map_2.append(bina)
    
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if map_1[i][j] == '0' and map_2[i][j] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    
    return answer
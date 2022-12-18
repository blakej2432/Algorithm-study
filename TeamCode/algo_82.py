# 오픈채팅방

def solution(record):
    answer = []
    dict = {}
    a = list(map(lambda x : x.split(' '), record))
    
    for i in a:
        if i[0] == 'Enter' or i[0] == 'Change':
            dict[i[1]] = i[2]
    
    for i in a:
        if i[0] == 'Enter':
            answer.append(f'{dict[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(f'{dict[i[1]]}님이 나갔습니다.')
            
    return answer










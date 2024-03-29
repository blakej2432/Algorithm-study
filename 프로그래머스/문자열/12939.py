# 최대값과 최소값

def solution(s):
    answer = ''
    nums = s.split(' ')
    num_list = list(map(int, nums))
    
    min_num = min(num_list)
    max_num = max(num_list)
    
    answer = f'{min_num} {max_num}'
    return answer
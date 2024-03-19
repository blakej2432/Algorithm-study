# 두 수 뽑아서 더하기

def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            new_num = numbers[i] + numbers[j]
            if new_num not in result:
                result.append(new_num)
    
    result.sort()
    
    return result
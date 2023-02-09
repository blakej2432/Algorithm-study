# pseudo code
'''
숫자는 그대로 두고 알파벳이 들어올 때 마다 temp로 단어를 만든다.
해당 단어를 dict에서 검색해 value(수)로 바꿔준다.
'''

# my code
def solution(s):
    answer = ''
    temp = ''
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in num_dict:
                answer += num_dict[temp]
                temp = ''    
    return int(answer)

# others'
'''
answer.replace(key, value) 로 바로 문자열 안의 알파벳을 숫자로 바꾼다.
'''
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
# 압축

import string



def solution(msg):
    dict = {}

    for i, k in enumerate(string.ascii_uppercase):
        dict[k] = i+1

    idx = 0
    maxIdx = 26
    length = 0
    answer = []
    while True:
        length += 1
        if not msg[idx:idx+length] in dict:
            answer.append(dict[msg[idx:idx+length-1]])
            maxIdx += 1
            dict[msg[idx:idx+length]] = maxIdx
            idx += length-1
            length = 0
        else:
            if idx+length-1 == len(msg):
                answer.append(dict[msg[idx:idx+length-1]])
                break
    return answer
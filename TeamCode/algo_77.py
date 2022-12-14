# 비밀지도
     
def solution(n, arr1, arr2):
    map_1 = []
    for i in arr1:
        bina = format(i, 'b')

        if len(bina) != n:
            bina = '0'*(n-len(bina)) + bina

        map_1.append(bina)

    map_2 = []
    for i in arr2:
        bina = format(i, 'b')

        if len(bina) != n:
            bina = '0'*(n-len(bina)) + bina

        map_2.append(bina)

    new_map = []
    for i in range(len(map_1)):
        temp = ''
        for j in range(len(map_1)):
            if map_1[i][j] == '1' or map_2[i][j] == '1':
                temp = temp + '#'
            else:
                temp = temp + ' '
        new_map.append(temp)

    return new_map


# 다른 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# bin(i|j) 쓰기
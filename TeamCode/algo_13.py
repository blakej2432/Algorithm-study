# 행렬의 덧셈
# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요

def solution(arr1,arr2):
2
    answer = []
3
    for i in range(len(arr1)):
4
        temp = []
5
        for j in range(len(arr1[i])):
6
            temp.append(arr1[i][j] + arr2[i][j])
7
        answer.append(temp)
8
    return answer

# temp = [] 쓰는 법 잘 이용해야돼 무조건 answer 하나에다가 해결보려고하면 안되지


# np.array로 그냥 해결하는법. 속도 차이 없음

import numpy as np

def solution(arr1, arr2):
    answer = np.array(arr1,float) + np.array(arr2,float)

    return answer.tolist()





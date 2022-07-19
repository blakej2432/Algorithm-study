# 약수의 개수와 덧셈
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

def solution(left, right):
    hap = 0
    for i in range(left,right+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            hap += i
        else:
            hap -= i
    return hap

# 무조건 리스트 만들어서 넣을 생각하지말고 count = 0 바로 들어가면 좋잖아
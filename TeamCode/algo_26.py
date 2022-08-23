# 2016년
# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.


# 내 풀이
def solution(a, b):
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt = 0

    if a == 1:
        cnt += b - 1
    elif a == 2:
        cnt += 30 + b
    elif a == 3:
        cnt += 30 + 29 + b
    elif a == 4:
        cnt += 30 + 29 + 31 + b
    elif a == 5:
        cnt += 30 + 29 + 31 + 30 + b
    elif a == 6:
        cnt += 30 + 29 + 31 + 30 + 31 + b
    elif a == 7:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + b
    elif a == 8:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + 31 + b
    elif a == 9:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + b
    elif a == 10:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + b
    elif a == 11:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 +b
    elif a == 12:
        cnt += 30 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 +30 + b
    return days[cnt%7]



def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))

# 내가 쓴 코드를 정리해서 한번에 쓸 수 있는게 밑에 있는 방법. 더할 요소들을 리스트 만들어 놓고[:a-1] 인덱스 처리하면
# 일일이 매번 안써도 인덱스로 알아서 더해주잖아
# 가운데 글자 가져오기
# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항

def solution(s):

    length = len(s)
    if length % 2 == 0:
        return s[int(length / 2 - 1)] + s[int(length / 2)]
    else:
        return s[int(length / 2)]

# s[int(length):-int(length)] 이런식으로 인덱스에 -에 붙이는 방식 기억
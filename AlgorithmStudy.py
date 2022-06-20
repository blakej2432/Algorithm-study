# 세 정수를 입력받아 최대값 구하기

print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: 
   maximum = b
if c > maximum: 
   maximum = c

print(f'최댓값은 {maximum}입니다.')

print('이름을 입력하세요.: ', end='')
name = input()
print(f'안녕하세요? {name}님.')

# 이름을 입력받아 인사하기
name = input('이름을 입력하세요.: ')
print(f'안녕하세요? {name}님.')

int('17')
int('0b110',2)
int('0o75',8)
int('13',10)
int('0x3F', 16)
float('3.14')

# 세 정수의 최댓값 구하기

def max3(a,b,c):
    """a,b,c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: 
       maximum = b
    if c > maximum: 
       maximum = c
    return maximum # 최댓값 반환
        
print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(5,8,11) = {max3(5,8,11)}')

# 세 정수를 입력받아 중앙값 구하기 1

def med3(a,b,c):
    """a,b,c의 중앙값을 구하여 반환"""
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b


print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a,b,c)}입니다.')

# 세 정수를 입력받아 중앙값 구하기 2 --> 똑같은 걸 두번 하게 되는 비효율

def med3(a,b,c):
    """a,b,c의 중앙값을 구하여 반환(다른방법)"""
    if (b >=a and c<=a) or (b <=a and c>=a):
        return a
    elif (a > b and c<b) or (a < b and c> b):
        return b
    return c


# 입력받은 정수의 부호(양수, 음수) 출력하기

n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')


n = int(input('정수를 입력하세요.'))

if n == 1:
    print('A')
elif n ==2:
    print('B')
elif n ==3:
    print('C')
else:
    pass

a = x if x>y else y

print('c는 0입니다.' if c == 0 else 'c는 0이 아닙니다.')

# 1부터 n까지 정수의 합 구하기 1(while문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요: '))

sum = 0
i = 1

while i <=n:
    sum += i
    i += 1

print(f'1부터 n까지 합: {sum}')


# 1부터 n까지 정수의 합 구하기 2(for문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum=0
for i in range(1,n+1):
    sum += i

print(f'1부터 n까지 합 : {sum}')

iterable -> 반복할 수 있는 객체


# a 부터 b까지 정수의 합 구하기(for문)

print('a부터b까지 정수의 합 구합니다.: ')
a = int(input('정수 a 값: '))
b = int(input('정수 b 값: '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
sum = 0

for i in range(a, b+1):
    sum += i
    
print(f'합은 {sum}')

# a부터 b까지 정수의 합 구하기 1

print('a부터b까지 정수의 합 구합니다.: ')
a = int(input('정수 a 값: '))
b = int(input('정수 b 값: '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
sum = 0

for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)


# a부터 b까지 정수의 합 구하기 2

print('a부터b까지 정수의 합 구합니다.: ')
a = int(input('정수 a 값: '))
b = int(input('정수 b 값: '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬
sum = 0

for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end ='')
sum += b

print(sum)


# +와 - 번갈아 출력하기 1

n = 10

for i in range(n):
    if i % 2:
        print('-',end='')
    else:
        print('+',end='')
    print(i)
print()


# +와 - 번갈아 출력하기 2 더 좋은 프로그램

n = 11

for _ in range(n//2): # or range(1,n//2+1)
    print('+-', end='')

if n % 2: # 1값이 true, 0이 false
    print('+', end='')
print()


# *를 n개 출력하되 w개마다 줄바꿈하기 1

n = 17
w = 5

for i in range(n):
    print('*',end='')
    if i % w == w-1:
        print()
if n%w:
    print()


# *를n개 출력하되 w개마다 줄바꿈하기 2

n = 17
w = 5

for _ in range(n//w):
    print('*'*w)

rest = n%w
if rest:
    print('*'*rest)

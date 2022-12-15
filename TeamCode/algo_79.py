dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def arith(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += dict[mod] if mod in dict.keys() else str(mod) 
    return rev_base[::-1] 



def solution(n, t, m, p):
    i = 0
    num = '0'
    result = ''
    while len(result) < t:
    
        num += arith(i, n)
        result = num[p-1::m]
        i += 1
    return result[0:t]


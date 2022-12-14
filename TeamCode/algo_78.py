# 다트 게임

a = [0,1,2,3,4,5,6,7,8,9,10]
a = list(map(str, a))
a

dartResult = '1D2S#10S'
result_lst = []
cnt = 0

for i in range(len(dartResult)):
  if dartResult[i] in a:
    temp_num = int(dartResult[i])
  
  if i > 0 and dartResult[i-1].isdecimal() and dartResult[i].isdecimal():
    temp_num = int(dartResult[i-1] + dartResult[i])

  if dartResult[i] == 'S':
    temp_num = int(temp_num) ** 1
    result_lst.append(temp_num)
    cnt += 1

  if dartResult[i] == 'D':
    temp_num = int(temp_num) ** 2
    result_lst.append(temp_num)
    cnt += 1

  if dartResult[i] == 'T':
    temp_num = int(temp_num) ** 3
    result_lst.append(temp_num)
    cnt += 1

  if dartResult[i] == '*':
    if cnt == 1:
      result_lst[cnt-1] = result_lst[cnt-1] * 2
    else:
      result_lst[cnt-2] = result_lst[cnt-2] * 2
      result_lst[cnt-1] = result_lst[cnt-1] * 2

  if dartResult[i] == '#':
    result_lst[cnt-1] = result_lst[cnt-1] * (-1)
  print(result_lst)
sum(result_lst)


# 다른 사람 풀이

dartResult = '1D2S#10S'
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
   
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

solution(dartResult)

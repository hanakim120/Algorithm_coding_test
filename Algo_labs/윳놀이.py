# 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모

def count_yoot(arr):
  a, b, c, d = map(int,arr)
  sum = a + b + c + d
  if sum == 3:
    return 'A'
  elif sum == 2:
    return 'B'
  elif sum == 1:
    return 'C'
  elif sum == 0:
    return 'D'
  else:
    return 'E'
    
    
for i in range(3):
  arr = input().split()
  #print(arr)
  print(count_yoot(arr))

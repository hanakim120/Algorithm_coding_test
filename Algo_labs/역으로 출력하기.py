# 정수를 입력으로 받아 입력 받은 수를 거꾸로 출력

array_len = int(input())
array = list(map(int, input().split()))

for i in range(array_len-1,-1,-1):
  print(array[i], end=' ')
  
# reverse() 이용

length = int(input())
lists = list(map(int, input().split()))

lists.reverse()

for i in lists:
  print(i, end=" ")

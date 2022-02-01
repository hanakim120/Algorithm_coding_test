# 연속으로 맞추면 맞춘 개수만큼 누적해서 가산점
# 틀리면 0점

num = int(input())
array = list(map(int,input().split()))
count = 0
result = 0
for i in range(num):
  if array[i] == 1 :
    count += 1
    result += count
  elif array[i] == 0:
    count = 0
print(result)

# enumerate 사용한 풀이 

leng = int(input())
ls = list(map(int, input().split()))
  
score = 0
stack = 0

for i,aw in enumerate(ls):
  stack += 1
  if i == 0 and aw == 1:
    score += 1
  elif aw == 1 and ls[i-1] == 0:
    score += 1
  elif aw == 1 and ls[i-1] == 1:
    score += stack
  elif aw == 0:
    stack = 0
    
print(score)

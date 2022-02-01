n, s = map(int, input().split())

idx = 0
for i in range(n):# 0,1,2,3,4 -> 5번 반복
  l = []
  for j in range(0, idx+1):
    if s==10:
      s = 1
    l.append(str(s))
    s+=1
  if (i+1) % 2 != 0:
    l.reverse()
    l = [" "]*(n-(i+1)) + l
    print("".join(l))
  else:
    l = [" "]*(n-(i+1)) + l
    print("".join(l))
  idx+=2
  
  
  
tab_count = 0
# 5,3 
floor, start_num = map(int, input().split())
null_count= floor-1 # null_count = 4
num = start_num # 3
for i in range(floor,floor*2): # i 5 ~ 9
  for j in range(null_count): # j 0 ~ 3
    print(" ", end="")
  numbers = ""
  for k in range(i-null_count):
    if num > 9:
      num = 1
    numbers+=str(num)
    num+=1
  if i%2 != 0:
    numbers = numbers[::-1]
  print(numbers)
  null_count-=1

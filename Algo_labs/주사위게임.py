num = int(input())

sum_list = []

for i in range(num):
  sum = list(map(int,input().split()))
  sum.sort()
  # 세 주사위 눈이 같은 경우
  if sum[0] == sum[1] == sum[2]:
    sum_list.append(10000+sum[0]*1000)
   # 세 주사위 눈이 모두 다른 경우
  elif sum[0] != sum[1] != sum[2]:
    sum_list.append(max(sum))
    # 하나의 주사위 눈만 다른 경우
  else :
    sum_list.append(1000+sum[1]*100)
    
print(max(sum_list))

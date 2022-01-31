# 누적해서 저금하다 일정 금액을 넘으면 stop 

M = int(input())
save_money = 0
count = 0
for i in range(1,M+1):
  save_money += i
  count += 1
  if save_money >= M :
    print(count)
    break

date = int(input())
car_list = list(map(int,input().split()))

count = 0

for num in car_list:
  if num == date:
    count+=1    
    
print(count)

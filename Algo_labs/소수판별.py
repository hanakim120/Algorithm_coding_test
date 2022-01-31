
n = int(input())
count = 0

# for i in range(1,n+1):
#   if n % i == 0:
#     count += 1
#     if count > 2 :
#       print('NO')
#       break
#     elif (i == n) and (count == 2):
#       print('YES')
#       break

result = 'YES'
for i in range(2, n):
  if n % i == 0:
    result = 'NO'
print(result)

# 홀수는 더하고, 짝수는 빼기

A, B = map(int,input().split())

odd = []
even = []

for i in range(A,B+1):
  if i % 2 == 0:
    even.append(i)
  else :
    odd.append(i)

print(sum(odd)-sum(even))

# 이진수 만들기

N = int(input())

list = []
while True:
  list.append(N % 2)
  N = N // 2
  if N < 1:
    break
list.reverse()
print("".join(map(str, list)))

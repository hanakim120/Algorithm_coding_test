# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램

N, K = map(int, input().split())

idx = 0
val = 0 
for i in range(1,N+1):
  if N % i == 0 :
    idx += 1
    if idx == K :
      val = i
      break
print(val) 

# -*- coding: utf-8 -*-
# 에라토스테네스의 체 구현
import math

n = 5 # 2부터 1000까지의 모든 수에 대해 소수 판별

# 모든 수가 소수인 것으로 초기화 (True)
array = [True for i in range(n+1)]

# 2부터 n의 제곱근까지의 모든 수 확인
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True : # 소수면
        j = 2 
        while i*j <= n :
            array[i*j] = False
            j += 1

# 모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')
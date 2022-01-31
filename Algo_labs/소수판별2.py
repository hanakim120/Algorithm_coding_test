# 자연수n,m이 주어질 때, n부터m까지 존재하는 소수를 모두 출력

def is_prime_number(nums):
    for i in range(2, (nums//2)+1):
        if nums % i == 0:
    	    return False
    return True

n, m = map(int,input().split())
    
for i in range(n,m+1):# 1,2,3 ... 10
  if i == 1:
    continue
  if is_prime_number(i) :
    print(i,end=' ')

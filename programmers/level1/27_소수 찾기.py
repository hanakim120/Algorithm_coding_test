# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# def solution(n): # n = 9
#     answer = 0
#     for p in range(2,n+1):
#         if is_prime(p)==True :
#             answer += 1

#     return answer

# def is_prime(k):
#     for i in range(2,k):
#         if k % i == 0:
#             return False
#     return True

# 에라토스테네스의 체
def solution(n):
    num = set(range(2,n+1)) # 2부터 n+1까지의 집합
    for i in range(2,n+1): # 2부터 n까지 반복문
        if i in num: # 만약 i 가 num 안에 있으면
            num -= set(range(2*i,n+1,i)) # i의 배수는 num 에서 제외
    return len(num) # 남아있는 숫자의 개수가 소수의 개수

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
  

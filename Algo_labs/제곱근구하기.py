# runtime error...
# 제곱해서 N보다 작거나 같은 숫자들의 배열 만들기
# N = int(input())
# for i in range(1,N):
#   if i*i < N :
#     s.append(i)
# # 배열의 최댓값 + 1
# print(max(s)+1)

import math

num = int(input())
if str(math.sqrt(num)).isnumeric():
  print(val)
else:
  print(math.ceil(math.sqrt(num)))

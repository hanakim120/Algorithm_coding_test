# -*- coding: utf-8 -*-
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # ¸ğµç ¿ø¼Ò¸¦ Â÷·Ê´ë·Î Èü¿¡ »ğÀÔ
    for value in iterable : 
        heapq.heappush(h, value)
    # Èü¿¡ »ğÀÔµÈ ¸ğµç ¿ø¼Ò¸¦ Â÷·Ê´ë·Î ²¨³»¾î ´ã±â
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

for i in range(n) :
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
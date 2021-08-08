def solution(n):
    str_3 = ''
    while n > 0: 
        n, mod = divmod(n,3) #(몫, 나머지)
        str_3 += str(mod)
        
    return int(str_3,3)

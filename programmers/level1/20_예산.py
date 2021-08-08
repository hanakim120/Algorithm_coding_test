def solution(d, budget):
    answer = 0
    count = 0
    # d 를 오름차순 정렬
    d.sort()
    
    # 맨 앞부터 더해서 budget을 초과하지 않을때 
    for i in d :
        if answer + i <= budget :
            answer += i
            count += 1
        else :
            break
            
    return count

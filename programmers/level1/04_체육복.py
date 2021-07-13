def solution(n, lost, reserve):
    answer = 0
    
    # 잃어버리지 않았거나 잃어버렸지만 여분 있는 학생 먼저 계산
    
    for i in range(1, n+1):
        # 잃어버리지 않은 학생
        if i not in lost: 
            answer += 1
            
        # 잃어버렸지만 여분 있는 학생
        else:
            if i in reserve:
                answer += 1
                reserve.remove(i)
                lost.remove(i)
                
    # 잃어버려서 빌려야 하는 학생
    for i in lost: 
        if i-1 in reserve: # 앞 번호
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve: # 뒷 번호
            answer +=1
            reserve.remove(i+1)

    return answer

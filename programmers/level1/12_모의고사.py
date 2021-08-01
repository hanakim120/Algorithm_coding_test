def solution(answers):
    answer = []
    score1 = 0
    score2 = 0
    score3 = 0
    student1 = [1,2,3,4,5] * 2000
    student2 = [2,1,2,3,2,4,2,5] * 1250
    student3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    # 학생 별 맞춘 문제 수 세기
    for i in range(len(answers)) :
        if student1[i] == answers[i]:
            score1 += 1
        if student2[i] == answers[i]:
            score2 += 1
        if student3[i] == answers[i]:
            score3 += 1
            
    # 가장 많이 맞춘 문제 수 저장   
    max_score = max(score1,score2,score3)
    
    # 가장 많이 맞춘 학생 찾기
    if max_score == score1 : 
        answer.append(1)
    if max_score == score2 : 
        answer.append(2)
    if max_score == score3 : 
        answer.append(3)
        
    # 정렬
    answer.sort()
        
    return answer

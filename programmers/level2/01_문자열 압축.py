def solution(s):
    length = []
    result = ""
    
    if len(s) == 1: # 문자열 s 가 1개인 경우
        return 1 # 무조건 1일 반환
    
    for cut in range(1, len(s) // 2 + 1): # 문자열 길이의 절반만큼 자르기 반복
        count = 1 
        temp = s[:cut] # 자르는 단위 문자열, 초기값 설정
        for i in range(cut, len(s), cut): # 단위문자열 길이씩 자르기
            if s[i:i+cut] == temp: # 문자열비교, 앞 문자열과 같으면
                count += 1 # count에 +1 
            else: # 앞 문자열과 다르면 
                if count == 1: 
                    count = "" # count 가 1이면 생략
                result += str(count) + temp # 문자열 요약
                temp = s[i:i+cut]
                count = 1

        if count == 1: 
            count = "" # count 가 1이면 생략
        result += str(count) + temp # 문자열 요약
        length.append(len(result)) 
        result = ""
    
    return min(length) # 결과 길이 중 가장 작은 값 반환

# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    answer = []
    element = []
    
    # element에 각 문자열의 인덱스 n번째 글자 넣기
    for x in strings :
        element.append(x[n])
    # 각 문자열의 인덱스 n번째 글자 중 겹치는 글자가 없을 때 sort
    if len(element) == len(set(element)) :
        answer = sorted(strings, key = lambda i : i[n])
        
    # 각 문자열의 인덱스 n번째 글자 중 겹치는 글자가 있을 때 사전 순 sort 후 또 한번 sort  
    else :
        answer = sorted(sorted(strings), key = lambda i : i[n])
    return answer

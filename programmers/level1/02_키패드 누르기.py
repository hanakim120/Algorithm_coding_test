def solution(numbers, hand):
    answer = ''

    # 키패드 자판 좌표료 표현하기
    keypand = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    # 시작 위치
    left_s = keypand['*']
    right_s = keypand['#']

    for i in numbers:
        now = keypand[i]
        
        # 1, 4, 7을 누르는 경우 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_s = now

        # 3, 6, 9를 누르는 경우 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_s = now

        # 2, 5, 8, 0을 누르는 경우 
        else:
            # 거리 초기값 설정
            left_d = 0
            right_d = 0

            # 거리 계산
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a - c)
                right_d += abs(b - c)

            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_s = now

            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_s = now

            # 거리 같은 경우
            else:
                # 왼손잡이
                if hand == 'left':
                    answer += 'L'
                    left_s = now

                # 오른손잡이
                else:
                    answer += 'R'
                    right_s = now

    return answer

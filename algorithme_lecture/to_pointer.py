# -*- coding: utf-8 -*-
n = 5 # ������ ����
m = 5 # ã���� �ϴ� �κ��� M
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

# start�� ���ʴ�� ������Ű�� �ݺ�
for start in range(n):
    # end �� ������ ��ŭ �̵�
    while interval_sum <m and end < n :
        interval_sum += data[end]
        end += 1
    # �κ����� m �� �� ī��Ʈ ����
    if interval_sum == m :
        count += 1
    interval_sum -= data[start]

print(count)

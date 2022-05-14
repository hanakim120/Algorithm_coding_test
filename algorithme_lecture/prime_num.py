# -*- coding: utf-8 -*-
# �����佺�׳׽��� ü ����
import math

n = 5 # 2���� 1000������ ��� ���� ���� �Ҽ� �Ǻ�

# ��� ���� �Ҽ��� ������ �ʱ�ȭ (True)
array = [True for i in range(n+1)]

# 2���� n�� �����ٱ����� ��� �� Ȯ��
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True : # �Ҽ���
        j = 2 
        while i*j <= n :
            array[i*j] = False
            j += 1

# ��� �Ҽ� ���
for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')
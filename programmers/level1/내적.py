def solution(a, b):
    x = []
    for i in range(len(a)):
        x.append(a[i]*b[i])
    return sum(x)

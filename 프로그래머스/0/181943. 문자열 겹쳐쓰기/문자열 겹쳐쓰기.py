def solution(a, b, s):
    x = a[:s] + b + a[s+len(b):]
    return x



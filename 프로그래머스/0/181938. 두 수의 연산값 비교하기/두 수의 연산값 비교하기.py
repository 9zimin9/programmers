def solution(a, b):
    str_a=str(a)
    str_b=str(b)
    
    ab= str_a+ str_b
    
    if int(ab) >= 2*a*b:
        return int(ab)
    else:
        return 2*a*b
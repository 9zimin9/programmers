from math import gcd

def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2

    # 최대공약수로 기약 분수 만들기
    divisor = gcd(a, b)
    a //= divisor
    b //= divisor

    return [a, b]


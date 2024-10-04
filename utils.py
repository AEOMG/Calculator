def radians(degrees): # 각도를 라디안으로 변환
    return degrees * (3.141592653589793 / 180)

def sin(x): # 테일러 급수를 이용한 사인 계산
    result = 0
    term = x
    n = 1
    while abs(term) > 1e-10:
        result += term
        term *= -x**2 / ((2 * n) * (2 * n + 1))
        n += 1
    return result

def cos(x): # 테일러 급수를 이용한 코사인 계산
    result = 0
    term = 1
    n = 0
    while abs(term) > 1e-10:
        result += term
        term *= -x**2 / ((2 * n + 1) * (2 * n + 2))
        n += 1
    return result
from utils import sin, cos, radians

class EngineeringCalculator:
    def __init__(self):
        super().__init__()

    def power(self, base, exp): # 제곱 계산
        result = 1
        for _ in range(abs(exp)):
            result *= base
        if exp < 0:
            result = 1 / result
        return result
    
    def sin(self, degrees): # 사인 계산
        rad = radians(degrees)
        return sin(rad)
    
    def cos(self, degrees): # 코사인 계산
        rad = radians(degrees)
        return cos(rad)

    def tan(self, degrees): # 탄젠트 계산
        cos_value = self.cos(degrees)
        if cos_value == 0:
            raise ValueError("이 값에서는 탄젠트를 계산할 수 없습니다.")
        return self.sin(degrees) / cos_value
    
    def sqrt(self, value): # 제곱근 구하기 
        if value < 0:
            raise ValueError("음수의 제곱근을 계산할 수 없습니다.")
        return self._newton_sqrt(value)
    
    def _newton_sqrt(self, value): # 뉴턴-랩슨 제곱근 사용
        guess = value / 2.0
        tolerance = 1e-10
        while abs(guess * guess - value) > tolerance:
            guess = (guess + value / guess) / 2.0
        return guess
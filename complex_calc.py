import math

class ComplexCalculator:
    def add(self, c1, c2):
        """복소수 덧셈: c1 + c2"""
        real = c1[0] + c2[0]
        imag = c1[1] + c2[1]
        return (real, imag)

    def subtract(self, c1, c2):
        """복소수 뺄셈: c1 - c2"""
        real = c1[0] - c2[0]
        imag = c1[1] - c2[1]
        return (real, imag)

    def multiply(self, c1, c2):
        """복소수 곱셈: c1 * c2"""
        real = c1[0] * c2[0] - c1[1] * c2[1]
        imag = c1[0] * c2[1] + c1[1] * c2[0]
        return (real, imag)

    def divide(self, c1, c2):
        """복소수 나눗셈: c1 / c2"""
        denominator = c2[0] ** 2 + c2[1] ** 2
        if denominator == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominator
        imag = (c1[1] * c2[0] - c1[0] * c2[1]) / denominator
        return (real, imag)

    def magnitude(self, c):
        """복소수 절대값 (크기) 계산"""
        return math.sqrt(c[0] ** 2 + c[1] ** 2)

    def argument(self, c):
        """복소수 편각 (각도) 계산 (라디안 단위)"""
        return math.atan2(c[1], c[0])

    def to_polar(self, c):
        """직교 좌표계에서 극 좌표계로 변환"""
        r = self.magnitude(c)
        theta = self.argument(c)
        return (r, theta)

    def to_rectangular(self, r, theta):
        """극 좌표계에서 직교 좌표계로 변환"""
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        return (real, imag)
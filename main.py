from basic import Calculator
from complex_calc import ComplexCalculator
from engineering import EngineeringCalculator

def main():
    print("=== 계산기 프로그램 ===")
    expression = input("계산할 식을 입력하세요 (예: 3 + 4, 2^3, (1+2j) + (2+3j)): ")

    if is_complex_expression(expression):
        complex_calculator(expression)
    elif is_engineering_expression(expression):
        engineering_calculator(expression)
    else:
        basic_calculator(expression)

def is_complex_expression(expression):
    # 복소수 연산식 판별
    return 'j' in expression or 'J' in expression

def is_engineering_expression(expression):
    # 공학 계산식 판별 (거듭제곱, 삼각함수 등)
    return '^' in expression or any(func in expression for func in ['sin', 'cos', 'tan', 'sqrt'])

def basic_calculator(expression):
    calc = Calculator()
    try:
        # 기본 사칙 연산 처리
        result = eval(expression)
        print(f"결과: {result}")
    except Exception as e:
        print(f"잘못된 식입니다: {e}")

def engineering_calculator(expression):
    eng_calc = EngineeringCalculator()
    try:
        # 공학용 계산식 처리
        if '^' in expression:
            base, exp = expression.split('^')
            result = eng_calc.power(float(base.strip()), int(exp.strip()))
        elif 'sin' in expression:
            degrees = float(expression.replace('sin', '').strip())
            result = eng_calc.sin(degrees)
        elif 'cos' in expression:
            degrees = float(expression.replace('cos', '').strip())
            result = eng_calc.cos(degrees)
        elif 'tan' in expression:
            degrees = float(expression.replace('tan', '').strip())
            result = eng_calc.tan(degrees)
        elif 'sqrt' in expression:
            value = float(expression.replace('sqrt', '').strip())
            result = eng_calc.sqrt(value)
        print(f"결과: {result}")
    except Exception as e:
        print(f"잘못된 식입니다: {e}")

def complex_calculator(expression):
    complex_calc = ComplexCalculator()
    try:
        # 복소수 연산 처리
        result = eval(expression)
        print(f"결과: {result}")
    except Exception as e:
        print(f"잘못된 식입니다: {e}")

if __name__ == '__main__':
    main()
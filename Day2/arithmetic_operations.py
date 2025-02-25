def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b

if __name__ == '__main__':
    # 테스트 코드
    print("Add: 3 + 5 =", add(3, 5))
    print("Add: -1 + 1 =", add(-1, 1))
    print("Subtract: 10 - 5 =", subtract(10, 5))
    print("Subtract: 0 - 7 =", subtract(0, 7))
    print("Multiply: 4 * 3 =", multiply(4, 3))
    print("Multiply: -2 * 6 =", multiply(-2, 6))
    print("Divide: 10 / 2 =", divide(10, 2))
    print("Divide: 9 / 3 =", divide(9, 3))

    try:
        print("Divide: 5 / 0 =", divide(5, 0))
    except ValueError as e:
        print("Error:", e)
def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def gugudan():
    print("\n".join([" ".join([f"{i}x{j}={i * j:2}" for j in range(1, 10)]) for i in range(1, 10)]))


# 테스트 코드
if __name__ == "__main__":
    operations = [
        ("Add", add, [(3, 5), (-1, 1)]),
        ("Subtract", subtract, [(10, 5), (0, 7)]),
        ("Multiply", multiply, [(4, 3), (-2, 6)]),
        ("Divide", divide, [(10, 2), (9, 3)])
    ]

    for name, func, cases in operations:
        for a, b in cases:
            print(f"{name}: {a} {func.__name__} {b} = {func(a, b)}")

    try:
        print("Divide: 5 / 0 =", divide(5, 0))
    except ValueError as e:
        print("Error:", e)

    gugudan()

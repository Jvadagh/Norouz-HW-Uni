def sin(x: float, N: int = 10):
    s = 0
    for i in range(N):
        s += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
    return s


def factorial(d):
    f = 1
    for n in range(1, d + 1):
        f = n * f

    return f


if __name__ == '__main__':
    x = float(input("insert x to calculate sin(x) : "))
    print(sin(x))

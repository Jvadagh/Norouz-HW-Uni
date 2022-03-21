# x^3 - x^2 + 2
def func(x):
    return x * x * x - x * x + 2


# Derivative of x^3 - x^2 + 2
def derivFunc(x):
    return 3 * x * x - 2 * x


# Function to find the root
def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ", x)


x0 = -20  # Initial values assumed
newtonRaphson(x0)
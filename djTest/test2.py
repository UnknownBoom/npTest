def productFib(prod):
    l = 0
    c = 0
    res = []
    g = fib()
    for i in range(3):
        print(next(g))
    return  c


def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

print(productFib(2))

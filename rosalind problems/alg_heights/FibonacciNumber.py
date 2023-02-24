def FibonacciLoop(number):
    old = 1
    new = 1
    for itr in range(number-1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new


def FibonacciLoopPythonic(number):
    old, new = 1, 1
    for itr in range(number-1):
        new, old = old, old + new
    return new


print(FibonacciLoop(10))
print(FibonacciLoopPythonic(10))
